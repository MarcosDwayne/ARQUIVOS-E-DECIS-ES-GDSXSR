"""Edição com controle de alterações do Word para o Assessor GDSXSR.

Toda inserção é gravada como alteração rastreada (w:ins) com a fonte já na cor 808080:
ao aceitar a alteração no Word, o texto novo permanece cinza. Exclusões viram w:del;
cisões e parágrafos novos marcam a marca de parágrafo como inserida; alinhamento vira
w:pPrChange e negrito/realce viram w:rPrChange.

v6 (06/10/2026): parágrafos com comentário também são reescritos (âncoras preservadas, C-54);
formatação rastreada de trecho/parágrafo (formatar_trecho, formatar_paragrafo); inserir_apos aceita
cor e formatação (resumo em vermelho, transcrições em itálico 13 com recuo 4/6).

Uso típico:
    from revisao_tracked import Revisor
    rv = Revisor(doc)                                  # doc = docx.Document(copia)
    rv.formatar_paragrafo(p, recuo_prim=4)             # recuo de 1ª linha 4 cm (C-41)
    rv.formatar_trecho(p, None, italico=True, tamanho=13)   # transcrição (C-40)
    rv.formatar_trecho(p, "Sem razão.", realce="YELLOW")   # ênfase (C-42/C-43)
    rv.inserir_apos(p, "texto", cor="EE0000", negrito=True)  # resumo em vermelho (C-39)
    rv.negritar(paragrafo, "nego provimento")         # (antes de reescrever o mesmo parágrafo)
    rv.reescrever(paragrafo, "novo texto")             # diff por palavra
    rv.reescrever(paragrafo, ["1º período.", "2º período."])  # troca + cisão, numa só chamada
    rv.inserir_apos(paragrafo, "texto novo")           # parágrafo novo
    rv.excluir(paragrafo)
    rv.alinhar(paragrafo, WD_ALIGN_PARAGRAPH.LEFT)
    doc.save(saida)
    aceitar_tudo("saida.docx", "aceito.docx")          # visão aceita, para conferência
"""
import copy, re, datetime, difflib, zipfile, tempfile, os, shutil
from docx import Document
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
from docx.shared import RGBColor
from docx.text.run import Run

AUTOR = "Assessor GDSXSR"
CINZA = RGBColor(0x80, 0x80, 0x80)
_ANCORAS = {qn("w:commentRangeStart"), qn("w:commentRangeEnd")}
_PERMITIDOS_P = {qn("w:pPr"), qn("w:r"), qn("w:bookmarkStart"), qn("w:bookmarkEnd"), qn("w:proofErr")} | _ANCORAS
_PERMITIDOS_R = {qn("w:rPr"), qn("w:t"), qn("w:tab"), qn("w:lastRenderedPageBreak"), qn("w:commentReference")}


def _eh_ref_comentario(el):
    return el.tag == qn("w:r") and el.find(qn("w:commentReference")) is not None
_ORDEM_PPR_FIM = [qn("w:rPr"), qn("w:sectPr"), qn("w:pPrChange")]


class ParagrafoProtegido(Exception):
    """Parágrafo com campo, hiperlink, nota ou imagem: não reescrever por inteiro (comentário não protege mais)."""


def _tokens(s):
    return re.findall(r"\s+|\w+|[^\w\s]", s, re.UNICODE)


class Revisor:
    def __init__(self, doc, autor=AUTOR, data=None):
        self.doc, self.autor = doc, autor
        self.data = data or datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
        ids = [int(e.get(qn("w:id"))) for e in doc.element.body.iter()
               if e.get(qn("w:id")) and e.get(qn("w:id")).lstrip("-").isdigit()]
        self._id = max(ids + [0]) + 1000

    # ---------- utilidades
    def _novo_id(self):
        self._id += 1
        return str(self._id)

    def _marca(self, tag):
        e = OxmlElement(tag)
        e.set(qn("w:id"), self._novo_id()); e.set(qn("w:author"), self.autor); e.set(qn("w:date"), self.data)
        return e

    def _verificar(self, p):
        for ch in p._p:
            if ch.tag not in _PERMITIDOS_P:
                raise ParagrafoProtegido(f"elemento {ch.tag.split('}')[1]} no parágrafo")
            if ch.tag == qn("w:r"):
                for rc in ch:
                    if rc.tag not in _PERMITIDOS_R:
                        raise ParagrafoProtegido(f"run com {rc.tag.split('}')[1]}")

    def _caracteres(self, p):
        """Lista (caractere, rPr) do texto atual do parágrafo."""
        out = []
        for r in p._p.findall(qn("w:r")):
            if _eh_ref_comentario(r):
                continue
            rpr = r.find(qn("w:rPr"))
            for c in r:
                if c.tag == qn("w:t"):
                    out += [(ch, rpr) for ch in (c.text or "")]
                elif c.tag == qn("w:tab"):
                    out.append(("\t", rpr))
        return out

    def _run(self, texto, rpr, apagado=False, cinza=False, paragrafo=None):
        r = OxmlElement("w:r")
        if rpr is not None:
            novo = copy.deepcopy(rpr)
            for ch in novo.findall(qn("w:rPrChange")):
                if apagado or cinza:
                    novo.remove(ch)
                else:
                    ch.set(qn("w:id"), self._novo_id())
            r.append(novo)
        partes = re.split(r"(\t)", texto)
        for parte in partes:
            if parte == "":
                continue
            if parte == "\t":
                r.append(OxmlElement("w:tab"))
            else:
                t = OxmlElement("w:delText" if apagado else "w:t")
                t.set(qn("xml:space"), "preserve"); t.text = parte
                r.append(t)
        if cinza:
            Run(r, paragrafo).font.color.rgb = CINZA
        return r

    def _grupos(self, chars):
        """Agrupa caracteres consecutivos com o mesmo rPr."""
        g = []
        for ch, rpr in chars:
            if g and g[-1][1] is rpr:
                g[-1][0].append(ch)
            else:
                g.append([[ch], rpr])
        return [("".join(a), b) for a, b in g]

    def _marcar_paragrafo(self, p_el, tag):
        ppr = p_el.find(qn("w:pPr"))
        if ppr is None:
            ppr = OxmlElement("w:pPr"); p_el.insert(0, ppr)
        rpr = ppr.find(qn("w:rPr"))
        if rpr is None:
            rpr = OxmlElement("w:rPr")
            fim = next((c for c in ppr if c.tag in (qn("w:sectPr"), qn("w:pPrChange"))), None)
            if fim is not None:
                fim.addprevious(rpr)
            else:
                ppr.append(rpr)
        rpr.insert(0, self._marca(tag))

    # ---------- operações
    def reescrever(self, p, novo, separador=True):
        """Reescreve o parágrafo em UMA operação: diff por palavra contra o texto atual.
        `novo` pode ser str ou lista de str; com lista, cada item vira um parágrafo (cisão rastreada),
        com parágrafo vazio de separação entre eles. Iguais ficam intactos, removidos em w:del,
        novos em w:ins cinza. Use uma única chamada por parágrafo original."""
        self._verificar(p)
        partes = [novo] if isinstance(novo, str) else list(novo)
        SEP = ""
        chars = self._caracteres(p)
        antigo = "".join(c for c, _ in chars)
        alvo = SEP.join(partes)
        if antigo == alvo:
            return 0
        ta, tn = _tokens(antigo), _tokens(alvo)
        pos, off = [], 0
        for t in ta:
            pos.append(off); off += len(t)
        pos.append(off)
        from docx.text.paragraph import Paragraph
        ppr = p._p.find(qn("w:pPr"))
        blocos = [[]]          # conteúdo de cada parágrafo resultante
        mudancas = 0
        def emitir_ins(texto, base):
            nonlocal blocos
            pedacos = texto.split(SEP)
            for n, ped in enumerate(pedacos):
                if n > 0:
                    blocos.append(None)   # marcador de quebra
                    blocos.append([])
                if ped:
                    ins = self._marca("w:ins")
                    ins.append(self._run(ped, base, cinza=True, paragrafo=p))
                    blocos[-1].append(ins)
        sm = difflib.SequenceMatcher(None, ta, tn, autojunk=False)
        for op, i1, i2, j1, j2 in sm.get_opcodes():
            a0, a1 = pos[i1], pos[i2]
            if op == "equal":
                for txt, rpr in self._grupos(chars[a0:a1]):
                    blocos[-1].append(self._run(txt, rpr))
                continue
            mudancas += 1
            if op in ("delete", "replace"):
                d = self._marca("w:del")
                for txt, rpr in self._grupos(chars[a0:a1]):
                    d.append(self._run(txt, rpr, apagado=True))
                blocos[-1].append(d)
            if op in ("insert", "replace"):
                base = chars[a0 - 1][1] if a0 > 0 else (chars[0][1] if chars else None)
                emitir_ins("".join(tn[j1:j2]), base)
        grupos = [b for b in blocos if b is not None]
        # âncoras de comentário (C-54 v6): preservadas — início no 1º parágrafo resultante, fim e referência no último
        inicios = [c for c in p._p if c.tag == qn("w:commentRangeStart")]
        fins = [c for c in p._p if c.tag == qn("w:commentRangeEnd")]
        refs = [c for c in p._p if _eh_ref_comentario(c)]
        # o último parágrafo reaproveita o elemento original (mantém a marca de parágrafo original)
        for ch in list(p._p):
            if ch.tag != qn("w:pPr"):
                p._p.remove(ch)
        if len(grupos) == 1:
            grupos[-1] = inicios + grupos[-1]
        else:
            grupos[0] = inicios + grupos[0]
        grupos[-1] = grupos[-1] + fins + refs
        for el in grupos[-1]:
            p._p.append(el)
        for conteudo in grupos[:-1]:
            np_ = OxmlElement("w:p")
            if ppr is not None:
                c = copy.deepcopy(ppr)
                for x in c.findall(qn("w:rPr")):
                    c.remove(x)
                for x in c.findall(qn("w:pPrChange")):
                    c.remove(x)
                np_.append(c)
            self._marcar_paragrafo(np_, "w:ins")
            for el in conteudo:
                np_.append(el)
            p._p.addprevious(np_)
            if separador:
                vazio = OxmlElement("w:p")
                if ppr is not None:
                    c = copy.deepcopy(ppr)
                    for x in c.findall(qn("w:rPr")) + c.findall(qn("w:pPrChange")):
                        c.remove(x)
                    vazio.append(c)
                self._marcar_paragrafo(vazio, "w:ins")
                p._p.addprevious(vazio)
        return mudancas

    def substituir(self, p, novo):
        return self.reescrever(p, novo)

    def cindir(self, p, inicio_segunda_parte, separador=True):
        texto = "".join(c for c, _ in self._caracteres(p))
        k = texto.find(inicio_segunda_parte)
        if k <= 0:
            raise ValueError("trecho da segunda parte não encontrado")
        return self.reescrever(p, [texto[:k].rstrip(" "), texto[k:]], separador)

    def inserir_apos(self, p, texto, separador=True, cor=None, **fmt):
        """Como _inserir_apos, com opções: cor (hex, padrão 808080; 'EE0000' só no resumo em vermelho, C-39),
        e formatação do texto/parágrafo novo: negrito, italico, sublinhado, tamanho (pt), realce ('YELLOW'),
        recuo_esq (cm), recuo_prim (cm), alinhamento (WD_ALIGN_PARAGRAPH)."""
        par = self._inserir_apos(p, texto, separador)
        from docx.shared import Pt, Cm
        from docx.enum.text import WD_COLOR_INDEX
        for r in par._p.iter(qn("w:r")):
            run = Run(r, par)
            if cor:
                run.font.color.rgb = RGBColor.from_string(cor.upper())
            if "negrito" in fmt: run.font.bold = fmt["negrito"]
            if "italico" in fmt: run.font.italic = fmt["italico"]
            if "sublinhado" in fmt: run.font.underline = fmt["sublinhado"]
            if "tamanho" in fmt: run.font.size = Pt(fmt["tamanho"])
            if fmt.get("realce"): run.font.highlight_color = getattr(WD_COLOR_INDEX, fmt["realce"])
        pf = par.paragraph_format
        if "recuo_esq" in fmt: pf.left_indent = Cm(fmt["recuo_esq"]) if fmt["recuo_esq"] is not None else None
        if "recuo_prim" in fmt: pf.first_line_indent = Cm(fmt["recuo_prim"]) if fmt["recuo_prim"] is not None else None
        if "alinhamento" in fmt: par.alignment = fmt["alinhamento"]
        return par

    def formatar_paragrafo(self, p, recuo_esq="manter", recuo_prim="manter", alinhamento="manter"):
        """Altera recuos (cm) e alinhamento com w:pPrChange (rastreado). None remove o recuo explícito."""
        from docx.shared import Cm
        ppr = p._p.get_or_add_pPr()
        antigo = OxmlElement("w:pPr")
        for c in ppr:
            if c.tag not in _ORDEM_PPR_FIM:
                antigo.append(copy.deepcopy(c))
        pf = p.paragraph_format
        if recuo_esq != "manter": pf.left_indent = Cm(recuo_esq) if recuo_esq is not None else None
        if recuo_prim != "manter": pf.first_line_indent = Cm(recuo_prim) if recuo_prim is not None else None
        if alinhamento != "manter": p.alignment = alinhamento
        velho = ppr.find(qn("w:pPrChange"))
        if velho is not None:            # mantém o estado original da 1ª alteração
            ppr.remove(velho)
            base = velho.find(qn("w:pPr"))
            if base is not None:
                antigo = copy.deepcopy(base)
        ch = self._marca("w:pPrChange"); ch.append(antigo)
        ppr.append(ch)

    def _isolar(self, p, trecho):
        """Divide, no lugar, os runs diretos do parágrafo para que `trecho` fique em runs próprios; devolve-os.
        Preserva âncoras de comentário e demais elementos."""
        if trecho is None:
            return [r for r in p._p.findall(qn("w:r")) if not _eh_ref_comentario(r) and r.find(qn("w:t")) is not None]
        runs = [r for r in p._p.findall(qn("w:r")) if not _eh_ref_comentario(r)]
        txt = "".join("".join(t.text or "" for t in r.findall(qn("w:t"))) for r in runs)
        k = txt.find(trecho)
        if k < 0:
            raise ValueError(f"trecho não encontrado: {trecho[:40]}")
        k1 = k + len(trecho)
        alvo, pos = [], 0
        for r in runs:
            ts = r.findall(qn("w:t"))
            s = "".join(t.text or "" for t in ts)
            a, b = pos, pos + len(s)
            pos = b
            if b <= k or a >= k1 or not s:
                continue
            if len(ts) != 1:           # run com tab/vários w:t: aplica no run inteiro
                alvo.append(r); continue
            i0, i1 = max(k, a) - a, min(k1, b) - a
            partes = [(s[:i0], False), (s[i0:i1], True), (s[i1:], False)]
            ref = r
            novos = []
            for texto, eh in partes:
                if not texto:
                    continue
                nr = copy.deepcopy(r)
                for t in nr.findall(qn("w:t")):
                    t.text = texto; t.set(qn("xml:space"), "preserve")
                novos.append((nr, eh))
            for nr, eh in novos:
                ref.addprevious(nr)
                if eh: alvo.append(nr)
            r.getparent().remove(r)
        return alvo

    def formatar_trecho(self, p, trecho=None, **props):
        """Formatação rastreada (w:rPrChange) do trecho (ou do parágrafo inteiro, trecho=None).
        props: negrito, italico, sublinhado (bool), tamanho (pt), cor (hex|None), realce ('YELLOW'|None)."""
        from docx.shared import Pt
        from docx.enum.text import WD_COLOR_INDEX
        for r in self._isolar(p, trecho):
            rp = r.find(qn("w:rPr"))
            antigo = OxmlElement("w:rPr")
            if rp is not None:
                for c in rp:
                    if c.tag != qn("w:rPrChange"):
                        antigo.append(copy.deepcopy(c))
                for c in rp.findall(qn("w:rPrChange")):
                    base = c.find(qn("w:rPr"))
                    if base is not None:     # mantém o estado original da 1ª alteração
                        antigo = copy.deepcopy(base)
                    rp.remove(c)
            run = Run(r, p)
            f = run.font
            if "negrito" in props: f.bold = props["negrito"]
            if "italico" in props: f.italic = props["italico"]
            if "sublinhado" in props: f.underline = props["sublinhado"]
            if "tamanho" in props: f.size = Pt(props["tamanho"])
            if "cor" in props:
                if props["cor"] is None:
                    c = r.find(qn("w:rPr") + "/" + qn("w:color"))
                    if c is not None: c.getparent().remove(c)
                else:
                    f.color.rgb = RGBColor.from_string(props["cor"].upper())
            if "realce" in props:
                f.highlight_color = getattr(WD_COLOR_INDEX, props["realce"]) if props["realce"] else None
            ch = self._marca("w:rPrChange"); ch.append(antigo)
            r.find(qn("w:rPr")).append(ch)

    def _inserir_apos(self, p, texto, separador=True):
        """Insere parágrafo novo (rastreado) depois de p, herdando o pPr; opcionalmente com parágrafo vazio antes.
        Segue a convenção do Word: a marca de parágrafo de p passa a ser a "nova" (inserida) e o último
        parágrafo criado recebe uma marca comum; ao rejeitar, tudo volta a ser apenas p."""
        from docx.text.paragraph import Paragraph
        ppr = p._p.find(qn("w:pPr"))
        def limpo():
            c = copy.deepcopy(ppr) if ppr is not None else OxmlElement("w:pPr")
            for x in c.findall(qn("w:pPrChange")):
                c.remove(x)
            r = c.find(qn("w:rPr"))
            if r is not None:
                for x in r.findall(qn("w:ins")) + r.findall(qn("w:del")):
                    r.remove(x)
            return c
        ja = p._p.find(qn("w:pPr") + "/" + qn("w:rPr") + "/" + qn("w:ins"))
        if ja is None:
            self._marcar_paragrafo(p._p, "w:ins")
        ref = p._p
        if separador:
            vazio = OxmlElement("w:p"); vazio.append(limpo())
            self._marcar_paragrafo(vazio, "w:ins")
            ref.addnext(vazio); ref = vazio
        novo = OxmlElement("w:p"); novo.append(limpo())
        chars = self._caracteres(p)
        base = chars[-1][1] if chars else None
        par = Paragraph(novo, p._parent)
        ins = self._marca("w:ins")
        ins.append(self._run(texto, base, cinza=True, paragrafo=par))
        novo.append(ins)
        ref.addnext(novo)
        return par

    def excluir(self, p):
        self._verificar(p)
        for r in list(p._p.findall(qn("w:r"))):
            for t in r.findall(qn("w:t")):
                t.tag = qn("w:delText")
            d = self._marca("w:del")
            r.addprevious(d); d.append(r)
        self._marcar_paragrafo(p._p, "w:del")

    def alinhar(self, p, alinhamento):
        ppr = p._p.get_or_add_pPr()
        antigo = OxmlElement("w:pPr")
        for c in ppr:
            if c.tag not in _ORDEM_PPR_FIM:
                antigo.append(copy.deepcopy(c))
        p.alignment = alinhamento
        ch = self._marca("w:pPrChange"); ch.append(antigo)
        ppr.append(ch)

    def negritar(self, p, trecho, negrito=True):
        """Aplica (ou retira) negrito, rastreado, ao trecho (preserva âncoras de comentário)."""
        return self.formatar_trecho(p, trecho, negrito=negrito)

    def _negritar_antigo(self, p, trecho, negrito=True):
        self._verificar(p)
        chars = self._caracteres(p)
        texto = "".join(c for c, _ in chars)
        k = texto.find(trecho)
        if k < 0:
            raise ValueError("trecho não encontrado")
        for ch in list(p._p):
            if ch.tag != qn("w:pPr"):
                p._p.remove(ch)
        for a, b, alvo in ((0, k, False), (k, k + len(trecho), True), (k + len(trecho), len(chars), False)):
            for txt, rpr in self._grupos(chars[a:b]):
                r = self._run(txt, rpr)
                if alvo:
                    rp = r.find(qn("w:rPr"))
                    antigo = OxmlElement("w:rPr")
                    if rp is not None:
                        for c in rp:
                            antigo.append(copy.deepcopy(c))
                    Run(r, p).font.bold = negrito
                    rch = self._marca("w:rPrChange"); rch.append(antigo)
                    r.find(qn("w:rPr")).append(rch)
                p._p.append(r)


# ---------- visão aceita (para o portão de entrega e para o comparador)
def _aceitar_xml(body):
    W = lambda t: qn("w:" + t)
    for d in list(body.iter(W("del"))):
        par = d.getparent()
        if par is not None and par.tag != W("rPr"):
            par.remove(d)
    for i in list(body.iter(W("ins"))):
        par = i.getparent()
        if par is not None and par.tag != W("rPr"):
            idx = par.index(i)
            for c in list(i):
                par.insert(idx, c); idx += 1
            par.remove(i)
    for tag in ("pPrChange", "rPrChange"):
        for e in list(body.iter(W(tag))):
            e.getparent().remove(e)
    for p in list(body.iter(W("p"))):
        rpr = p.find(W("pPr") + "/" + W("rPr"))
        if rpr is None:
            continue
        for i in rpr.findall(W("ins")):
            rpr.remove(i)
        d = rpr.find(W("del"))
        if d is not None:
            rpr.remove(d)
            nxt = p.getnext()
            if nxt is not None and nxt.tag == W("p"):
                pos = 1 if nxt.find(W("pPr")) is not None else 0
                for c in [c for c in p if c.tag != W("pPr")]:
                    nxt.insert(pos, c); pos += 1
            p.getparent().remove(p)


def aceitar_tudo(entrada, saida):
    d = Document(entrada)
    _aceitar_xml(d.element.body)
    d.save(saida)
    return saida


def contar_alteracoes(path):
    with zipfile.ZipFile(path) as z:
        x = z.read("word/document.xml")
    return {t: x.count(f"<w:{t} ".encode()) for t in ("ins", "del", "pPrChange", "rPrChange")}


def insercoes_sem_cinza(path, permitidas=("808080",)):
    """Runs inseridos (w:ins) cuja cor não está em `permitidas` — deve ser zero.
    O portão passa ("808080", "EE0000") e confere à parte que o vermelho só aparece no resumo (C-39)."""
    permitidas = {c.upper() for c in permitidas}
    d = Document(path)
    ruins = []
    for ins in d.element.body.iter(qn("w:ins")):
        if ins.getparent().tag == qn("w:rPr"):
            continue
        for r in ins.findall(qn("w:r")):
            cor = r.find(qn("w:rPr") + "/" + qn("w:color"))
            if cor is None or cor.get(qn("w:val")).upper() not in permitidas:
                ruins.append("".join(t.text or "" for t in r.iter(qn("w:t")))[:60])
    return ruins
