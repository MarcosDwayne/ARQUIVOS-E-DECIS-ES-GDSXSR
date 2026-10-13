#!/usr/bin/env python3
"""Portão automático GDSXSR (v6, 06/10/2026): python3 checar_voto.py REVISADO.docx [ORIGINAL.docx] [--classe=APC|AGI|EMD]
Analisa a versão ACEITA do documento (controle de alterações) e exige revisao_tracked.py na mesma pasta.
v6: formatação do manual e da estrutura pronta (recuo 4 cm; transcrições Arial 13 itálico, recuo 4/6;
ementas sem recuo de 1ª linha; enumeração em negrito; ID no singular; mini-dispositivo sublinhado e ausente
no último capítulo; resumo em vermelho; sentença em verde; comentários que deixam decisão ao assessor)."""
import sys, re, hashlib, zipfile, os, tempfile
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from revisao_tracked import aceitar_tudo, contar_alteracoes, insercoes_sem_cinza
from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH

args = [a for a in sys.argv[1:] if not a.startswith("--")]
classe = next((a.split("=")[1] for a in sys.argv[1:] if a.startswith("--classe=")), "APC").upper()
rev_path = args[0]; orig_path = args[1] if len(args) > 1 else None

FIXAS = {"com razão.", "sem razão.", "com parcial razão.", "com razão em parte.", "é o relatório.",
         "é como voto.", "ementa", "relatório", "voto", "dispositivo"}
LIM = {"APC": (20, 45, 58), "AGI": (20, 45, 55), "EMD": (20, 40, 50)}[classe]
alertas = []; _vist = set()
def A(nivel, sec, i, msg, txt=""):
    if (sec, i, msg) in _vist: return
    _vist.add((sec, i, msg)); alertas.append(f"[{nivel}] {sec} §{i}: {msg}" + (f" → «{txt[:90]}»" if txt else ""))

def cm(v): return round(v.cm, 1) if v is not None else None

def transcricao(p):
    t = p.text.strip()
    ind = p.paragraph_format.left_indent
    tam = {r.font.size.pt for r in p.runs if r.font.size}
    return (t[:1] in "\"“'" or (ind is not None and ind.cm >= 2) or tam == {13.0} or "– Grifei" in t)

def secao_de(t):
    u = t.strip().upper()
    for s in ("EMENTA", "RELATÓRIO", "VOTO", "DISPOSITIVO"):
        if u == s: return s
    return None

cont = contar_alteracoes(rev_path)
rastreado = sum(cont.values()) > 0
aval_path = rev_path
if rastreado:
    aval_path = os.path.join(tempfile.mkdtemp(), "aceito.docx")
    aceitar_tudo(rev_path, aval_path)
    for t in insercoes_sem_cinza(rev_path, permitidas=("808080", "EE0000")):
        A("ERRO", "CONTROLE", 0, "inserção rastreada sem cor 808080 (C-44)", t)
d = Document(aval_path)
ps = d.paragraphs
sec, micro_seq = "CABEÇALHO", 0
vistos = set()
anexo = False          # depois de "É como voto." vem a sentença anexada
resumo = False         # bloco RESUMO … até RELATÓRIO
tem_resumo = False
ultimo_editorial = None
anexo_nao_verde = 0
for i, p in enumerate(ps):
    t = p.text.strip()
    s = secao_de(t)
    if t.upper().startswith("RESUMO DA APELAÇÃO") or t.upper().startswith("RESUMO DO AGRAVO") or t.upper().startswith("RESUMO DA DECISÃO") or t.upper().startswith("RESUMO DOS EMBARGOS"):
        resumo = True; tem_resumo = True; continue
    if s:
        resumo = False
        if s == "DISPOSITIVO" and ultimo_editorial is not None:
            j, tt = ultimo_editorial
            if re.search(r"nesse ponto|neste ponto", tt, re.I):
                A("AVISO", "VOTO", j, "último capítulo não leva mini-dispositivo; suprimir (C-3A, manual 2.3.6)", tt)
        sec = s; vistos.add(s); micro_seq = 0
        if s == "EMENTA" and p.alignment == WD_ALIGN_PARAGRAPH.CENTER:
            A("ERRO", sec, i, "título EMENTA centralizado (deve ficar à esquerda)")
        if s == "DISPOSITIVO" and not any(r.bold for r in p.runs if r.text.strip()):
            A("ERRO", sec, i, "título DISPOSITIVO sem negrito")
        continue
    if not t or sec == "CABEÇALHO":
        continue
    if t == "É como voto.":
        anexo = True; continue
    runs = [r for r in p.runs if r.text.strip()]
    if anexo:
        if any(not (r.font.color and r.font.color.rgb and str(r.font.color.rgb).upper() in ("00B050", "008000")) for r in runs):
            anexo_nao_verde += 1
        continue
    # vermelho fora do resumo
    if not resumo and any(r.font.color and r.font.color.type is not None and r.font.color.rgb is not None
                          and str(r.font.color.rgb).upper() in ("EE0000", "FF0000") for r in runs):
        A("ERRO", sec, i, "vermelho fora do resumo (cor exclusiva do Desembargador, manual 2.3.9)", t)
    if resumo:
        continue
    trans = transcricao(p)
    pf = p.paragraph_format
    # fontes
    for r in runs:
        if r.font.name and r.font.name != "Arial":
            A("AVISO", sec, i, f"fonte {r.font.name} (padrão Arial)", t); break
        if r.font.size and not trans and r.font.size.pt not in (14.0,):
            A("AVISO", sec, i, f"corpo {r.font.size.pt} pt (texto editorial = 14)", t); break
    # ementa
    if sec == "EMENTA":
        if re.match(r"^(I|II|III|IV)\.\s", t) and p.alignment == WD_ALIGN_PARAGRAPH.CENTER:
            A("ERRO", sec, i, "título da ementa centralizado", t)
        if t.startswith("Tese de julgamento"):
            A("AVISO", sec, i, "a estrutura pronta não traz 'Tese de julgamento'; suprimir salvo tese nova fixada no voto (C-37)", t)
        if re.match(r"^(A|O)\s+(autora?|ré|réu|apelante|agravante|embargante)", t) and i > 0 and "Caso em exame" in "\n".join(x.text for x in ps[max(0, i-4):i]):
            A("AVISO", sec, i, "item da ementa sem numeração (o item 3 também é numerado, C-36)", t)
        for rot in ("Dispositivos relevantes citados:", "Jurisprudência relevante citada:"):
            if t.startswith(rot):
                rr = [r for r in runs if r.text.strip()]
                if rr and not rr[0].italic:
                    A("AVISO", sec, i, f"rótulo '{rot}' em itálico (estrutura pronta, C-40)", t)
        continue
    # recuos e transcrições (manual 2.3.2)
    if sec in ("RELATÓRIO", "VOTO", "DISPOSITIVO"):
        titulo = t.isupper() and len(t.split()) <= 18
        if trans:
            if any(r.font.size and r.font.size.pt != 13.0 for r in runs) or any(r.italic is False or r.italic is None for r in runs if len(r.text.strip()) > 3):
                A("AVISO", sec, i, "transcrição deve ser Arial 13 em itálico (C-40)", t)
            if cm(pf.left_indent) != 4.0:
                A("AVISO", sec, i, f"transcrição com recuo esquerdo {cm(pf.left_indent)} cm (padrão 4 cm, C-41)", t)
            if re.match(r"^“?[A-ZÀ-Ú ,.ºª0-9/-]{25,}\.", t) and t.upper() == t[:len(t)].upper()[:len(t)] and t[:60].isupper():
                A("AVISO", sec, i, "transcrição de ementa com cabeçalho; suprimir com “(...)” (manual 2.3.2, C-62)", t)
        elif not titulo and cm(pf.first_line_indent) != 4.0 and not t.startswith("O Senhor Desembargador"):
            A("AVISO", sec, i, f"recuo de 1ª linha {cm(pf.first_line_indent)} cm (texto normal: 4 cm, C-41)", t)
        if trans:
            micro_seq = 0; continue
    # enumeração em negrito (manual 2.3.5)
    for m in re.finditer(r"(?:^|[:;]\s|\s)(\d{1,2}\))(?=\s+[a-zà-úA-ZÀ-Ú])", t):
        alvo = m.group(1)
        if not any(alvo in r.text and r.bold for r in p.runs):
            A("AVISO", sec, i, "números da enumeração das alegações em negrito (C-43)", t); break
    # expressões vedadas
    for pat, msg in [(r"\ba minuta (aponta|indica|demonstra)|\ba revisão (demonstrou|indica)", "minuta/revisão citada como fonte"),
                     (r"Requer o não provimento", "suprimir 'Requer o não provimento' (v4)"),
                     (r"\bademais\b", "preferir 'no mais' (v4)"),
                     (r"\bIDs\b|\bID\.\s", "ID sempre no singular e sem ponto (manual, C-25)"),
                     (r"\b(restou|restaram) (comprovad|demonstrad)", "'restar' por 'estar' (manual)"),
                     (r"\b(outrossim|destarte|dessarte|porquanto|mormente|inobstante)\b", "expressão vedada pelo manual"),
                     (r"^(Nos termos|Conforme|De acordo com|Segundo) (d?o |d?a )?(art\.|artigo|§)", "dispositivo legal no início do período; levar ao final entre parênteses")]:
        if re.search(pat, t, re.I): A("AVISO", sec, i, msg, t)
    # ID / artigo no meio do período
    formula = re.match(r"^(Apelo d|Agravo d|Embargos d|Contrarrazões|Contraminuta|Condeno|Majoro|Fixo)", t) or re.search(r"\b1\) ", t)
    for m in ([] if formula else re.finditer(r"\((ID[^)]*|[A-Z]{2,4} \d+[^)]*)\)", t)):
        resto = t[m.end():m.end()+3]
        if resto and not re.match(r"^[\s]*[.;:]|^$|^\s*–", resto) and re.match(r"^\s*[a-zà-ú,]", resto):
            A("AVISO", sec, i, f"referência {m.group(0)} no meio do período", t)
    # mini-dispositivo sublinhado (manual 2.3.6)
    if sec == "VOTO" and re.match(r"^(Assim, )?(Rejeito|Acolho|Nego provimento|Dou (parcial )?provimento)", t) and len(t.split()) < 30:
        if not all(r.underline for r in runs if len(r.text.strip()) > 1):
            A("AVISO", sec, i, "mini-dispositivo do capítulo sublinhado (C-3A)", t)
    if sec == "DISPOSITIVO":
        for verbo in ("Condeno", "Majoro", "Fixo", "Inverto", "Redistribuo"):
            if t.startswith(verbo) and not any(r.bold and verbo in r.text for r in runs):
                A("AVISO", sec, i, f"'{verbo}' em negrito no dispositivo (estrutura pronta, C-43)", t)
    # cadência (voto e relatório)
    n = len(t.split())
    periodos = len([x for x in re.split(r"(?<=[.!?])\s+(?=[A-ZÀ-Ú])", t) if x.strip()])
    fixa = t.lower() in FIXAS or t.lower().startswith(("presentes os pressupostos", "o senhor desembargador"))
    titulo = t.isupper() and n <= 18
    if sec in ("VOTO", "DISPOSITIVO") and not fixa and not titulo:
        if n < 15:
            micro_seq += 1
            if micro_seq >= 3: A("AVISO", sec, i, "3+ microparágrafos seguidos (<15 palavras)", t)
        else:
            micro_seq = 0
        if n > LIM[2] and not re.search(r"\b1\)", t): A("AVISO", sec, i, f"{n} palavras: provável >4 linhas renderizadas; cindir no ponto lógico", t)
        if sec == "VOTO" and periodos >= 2 and n > LIM[1]:
            A("INFO", sec, i, f"{periodos} períodos/{n} palavras: separar período conclusivo autônomo (v4)?", t)
    else:
        micro_seq = 0
    if sec == "VOTO" and titulo and not t.startswith(("APELO", "AGRAVO", "EMBARGOS", "REMESSA", "RECURSO")) \
            and p.alignment != WD_ALIGN_PARAGRAPH.CENTER:
        A("AVISO", sec, i, "subtítulo do voto não centralizado", t)
    if sec == "VOTO" and titulo and t.startswith("DA") and not any(r.font.highlight_color for r in runs):
        A("INFO", sec, i, "subtítulo de capítulo realçado em amarelo (C-42)", t)
    if sec in ("VOTO", "DISPOSITIVO"):
        ultimo_editorial = (i, t)

for s in ("EMENTA", "RELATÓRIO", "VOTO", "DISPOSITIVO"):
    if s not in vistos: A("ERRO", "ESTRUTURA", 0, f"título {s} não encontrado")
if classe in ("APC", "AGI", "EMD") and not tem_resumo:
    A("AVISO", "ESTRUTURA", 0, "falta o RESUMO … EM SENTIDO CONTRÁRIO AO VOTO, em vermelho, entre a ementa e o relatório (C-39)")
if anexo_nao_verde:
    A("AVISO", "ANEXO", 0, f"{anexo_nao_verde} parágrafo(s) da decisão anexada fora da cor verde 00B050 (C-45)")
txt = "\n".join(p.text for p in ps)
for f in ("É como voto.", "Ante o exposto"):
    if f not in txt: A("AVISO", "ESTRUTURA", 0, f"fórmula '{f}' ausente")
for s in ("I. Caso em exame", "II. Questão em discussão", "III. Razões de decidir", "IV. Dispositivo"):
    if s.lower() not in txt.lower(): A("AVISO", "EMENTA", 0, f"parte '{s}' ausente")

# integridade, comentários e comparação com o original
try:
    with zipfile.ZipFile(rev_path) as z:
        bad = z.testzip()
        cx = z.read("word/comments.xml").decode("utf8") if "word/comments.xml" in z.namelist() else ""
    n_com = cx.count("<w:comment ")
    if bad: A("ERRO", "DOCX", 0, f"ZIP corrompido em {bad}")
    for m in re.finditer(r'<w:comment [^>]*w:author="Revisor GDSXSR"[^>]*>(.*?)</w:comment>', cx, re.S):
        c = re.sub(r"<[^>]+>", "", m.group(1))
        if re.search(r"\b(decidir se|sugest[ãa]o|sugiro|avaliar se|considerar se|a crit[ée]rio)", c, re.I):
            A("ERRO", "COMENTÁRIOS", 0, "comentário do revisor deixa a decisão ao assessor; alterar o texto e explicar (C-54)", c[:120])
except Exception as e:
    A("ERRO", "DOCX", 0, f"falha ao abrir: {e}"); n_com = 0
if orig_path:
    o = Document(orig_path)
    print("hash original:", hashlib.sha256(open(orig_path, "rb").read()).hexdigest()[:16])
    if len(o.tables) != len(d.tables): A("ERRO", "DOCX", 0, f"tabelas: original {len(o.tables)} × revisado {len(d.tables)}")
    if o.tables and d.tables and [c.text for c in o.tables[0]._cells] != [c.text for c in d.tables[0]._cells]:
        A("AVISO", "CABEÇALHO", 0, "tabela de autuação difere do original; conferir")
    with zipfile.ZipFile(orig_path) as z:
        oc = z.read("word/comments.xml").count(b"<w:comment ") if "word/comments.xml" in z.namelist() else 0
    if n_com < oc: A("ERRO", "COMENTÁRIOS", 0, f"comentários diminuíram: {oc} → {n_com}")
    if not rastreado and [p.text for p in o.paragraphs] != [p.text for p in d.paragraphs]:
        A("ERRO", "CONTROLE", 0, "texto alterado sem controle de alterações (usar revisao_tracked.Revisor)")
    norm = lambda x: re.sub(r"\s+", " ", x).strip()
    dt = norm(" ".join(p.text for p in d.paragraphs))
    ot = [p.text.strip() for p in o.paragraphs if transcricao(p) and len(p.text.split()) > 8]
    perdidas = [t for t in ot if norm(t) not in dt and not t[:40].isupper()]
    for t in perdidas[:10]: A("AVISO", "TRANSCRIÇÃO", 0, "transcrição do original alterada; conferir se foi só supressão autorizada (cabeçalho de ementa)", t)

print(f"Classe {classe} | parágrafos (versão aceita) {len(ps)} | comentários {n_com} | alterações rastreadas {cont}")
for a in alertas: print(a)
erros = sum(a.startswith("[ERRO]") for a in alertas)
print(f"\nRESULTADO: {erros} erro(s), {len(alertas)-erros} aviso(s). " + ("REPROVADO" if erros else "Sem erros bloqueantes; examinar avisos."))
sys.exit(1 if erros else 0)
