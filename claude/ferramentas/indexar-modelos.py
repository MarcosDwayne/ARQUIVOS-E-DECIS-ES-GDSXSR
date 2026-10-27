#!/usr/bin/env python3
"""Gera o índice de modelos GDSXSR a partir das listagens do Drive (lst/ok/*.json)."""
import json, glob, re, csv, collections, unicodedata, os

PASTA = {'1pCGIBo7dAcI_8SUURdlwHhoEcY56P-Wb': ('OURO', 'APC'), '1yzaSbE1iWruEAA1HLQ0kEruQbAYm6Tw4': ('OURO', 'AGI'),
         '1TPrue7ddcjRBSSP-Vpduet7BQHmH48CV': ('OURO', 'EMD'), '1FpfJdjTI5yY6Jc0aTs0a9J-CNbhX7ayA': ('GERAIS', 'APC'),
         '1HsU4LR_TzG5486_qbEIam6i1yvGjDtNc': ('GERAIS', 'AGI'), '1cVC4zXcsalN0OwHWI8KA3SnuJzVuqiTy': ('GERAIS', 'EMD'),
         '1j830dPHkpLML9QShNuh5Xurbr-oKw029': ('LIMINARES', 'AGI')}
CLASSES = {'APC', 'AGI', 'EMD', 'AIN', 'RMO', 'MSG', 'APO', 'REO', 'RNE', 'AGR', 'AGT', 'ACP', 'CC', 'CCI', 'MS', 'AR', 'ARE', 'APL', 'AGINT', 'EDCIV', 'CCP', 'RCL'}
RESULT = {'NP', 'DP', 'DPP', 'DDP', 'NC', 'PNC', 'PP', 'NCP', 'CPNC', 'NPP'}
MARCAS = [('recorrigido', 'recorrigido'), ('corrigid', 'corrigido'), ('alterad', 'alterado'), ('ajustad', 'ajustado'),
          ('ajuste', 'ajustado'), ('aprovad', 'aprovado'), ('comentário', 'com comentário'), ('pref', 'preferência')]
CORRECAO = {'recorrigido', 'corrigido', 'alterado', 'ajustado', 'aprovado'}
NAO_NOMES = {'Des', 'Dec', 'Rel', 'Tema', 'PASEP', 'SUS', 'STJ', 'STF', 'MS', 'CDC', 'CPC', 'DF', 'TJDFT', 'INSS', 'IPTU',
             'Busca', 'Embargos', 'Desp', 'PJe', 'Dec', 'Jansen', 'Voto', 'Parecer', 'Ementa', 'Tema', 'Fusca', 'Corrigido', 'Recorrigido', 'Def', 'Indef', 'Revisado', 'Preferência', 'Pref', 'PV', 'ACA', 'NC'}

MATERIAS = [
    ('Família', r'alimento|guarda|uni[aã]o est[aá]vel|div[oó]rcio|partilha|paternidade|maternidade|curatela|conviv[eê]ncia|visita|poder familiar|filia[cç][aã]o|sobrepartilha|abandono afetivo'),
    ('Saúde', r'plano de sa[uú]de|home care|medicament|\bsus\b|cobertura|\btea\b|autis|cirurgia|tratamento|operadora|unimed|interna[cç]'),
    ('PASEP', r'pasep'),
    ('Bancário e consumidor', r'fraude|golpe|empr[eé]stimo|consignad|cart[aã]o|seguro|juros|revisional|banc|pix|superendivid|consumidor|negativa[cç]|serasa|scr\b|voo|a[eé]re|venda casada|tarifa'),
    ('Fazenda Pública e servidor', r'servidor|25.? ?hora|subs[ií]dio|\bgap\b|concurso|iptu|icms|difal|tribut|fazenda|distrito federal|\bdf\b|pens[aã]o por morte|iprev|magist[eé]rio|heteroidentif|demoli|ressarcimento ao er[aá]rio|mandado de seguran|\bms\b'),
    ('Execução e cumprimento', r'penhora|execu[cç]|cumprim|sisbajud|renajud|infojud|serasajud|teimosinha|desconsidera|arresto|bem de fam[ií]lia|contadoria|c[aá]lculo|rpv|precat[oó]rio|astreinte|multa coercitiva'),
    ('Processual', r'gratuidade|honor[aá]rio|prescri|extin[cç]|emenda|inicial|cerceamento|dialeticidade|compet[eê]ncia|foro|ilegitim|legitimid|intempestiv|desert|coisa julgada|preclus|nulidade|fundamenta[cç]|sucumb|interesse recursal|litig[aâ]ncia'),
    ('Posse e imóveis', r'usucapi|posse|reintegra|imiss[aã]o|despejo|loca[cç]|condom[ií]nio|reivindicat|im[oó]vel|terreno|lote'),
    ('Responsabilidade civil', r'dano moral|danos morais|indeniza|acidente|ve[ií]culo|responsabilidade civil|dano material'),
    ('Busca e apreensão', r'busca e apreens'),
    ('Contratos e obrigações', r'contrato|cobran[cç]a|m[uú]tuo|monit[oó]ria|cheque|nota promiss|compra e venda|presta[cç][aã]o de servi'),
]


def sem_acento(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')


def marcos_tmp(t):
    return ' marcos ' in f' {t.lower()} '


def analisar(x):
    pasta, classe_pasta = PASTA[x['parentId']]
    t = re.sub(r'\.(docx|doc)$', '', x['title'], flags=re.I).strip()
    tl = t.lower()
    toks = t.replace('–', ' ').replace('-', ' - ').split()
    m = re.search(r'(\d{7})\s*-\s*(\d{2})', t)
    proc = f'{m.group(1)}-{m.group(2)}' if m else ''
    # classe = primeira sigla conhecida no título
    classe = next((w.strip('.,()').upper() for w in t.split() if w.strip('.,()').upper() in CLASSES), classe_pasta)
    resto = t[m.end():] if m else t
    rt = resto.split()
    nomes, resultado, i = [], '', 0
    while i < len(rt):
        w = rt[i].strip('.,()-')
        if w.upper() in RESULT and w.isupper():
            resultado = 'DPP' if w.upper() == 'DDP' else w.upper(); i += 1; break
        if w in NAO_NOMES and not (w.upper() in RESULT and w.isupper()):
            i += 1; continue
        if w and w[0].isupper() and w not in NAO_NOMES and not w.isupper() and len(w) > 2 and w.isalpha() and len(nomes) < 4:
            nomes.append(w); i += 1; continue
        if w in ('-', '') or w.lower() in ('com', 'comentário', '(comentário)', 'alterado', 'corrigido'):
            i += 1; continue
        break
    assunto = ' '.join(rt[i:]).strip(' -')
    if not resultado:
        mm = re.search(r'\b(NP|DPP|DP|DDP|NC)\b', t)
        resultado = (mm.group(1).replace('DDP', 'DPP') if mm else '')
    tipo = 'voto'
    if re.search(r'\bdec\b|decis', tl): tipo = 'decisão'
    if re.search(r'\bdesp\b|despacho|intima', tl): tipo = 'despacho'
    if re.search(r'\bpv\b|voto vista|voto divergente|diverge rel', tl): tipo = 'voto-vista/divergente'
    # pasta LIMINARES: decisão monocrática do Relator sobre tutela/efeito suspensivo (o resultado vem das abreviaturas do título)
    if pasta == 'LIMINARES' and re.search(r'\b(def|indef|ant tut|ef susp|efeito susp|tut|tutela|medidas urgentes|liminar|defere|indefere)\b', tl):
        tipo = 'liminar'
        indef = re.search(r'\bindef', tl) is not None
        defer = re.search(r'\bdef(?!\w)|\bdefere|\bdefiro|\bdeferid', tl) is not None
        if 'medidas urgentes' in tl: resultado = 'MEDIDAS URGENTES'
        elif re.search(r'n[aã]o conhec|ñ conhec', tl): resultado = 'NÃO CONHECIDA'
        elif (defer and indef) or re.search(r'\bdef\s+par|\bparte\b', tl): resultado = 'DEFERIDA EM PARTE'
        elif indef: resultado = 'INDEFERIDA'
        elif defer: resultado = 'DEFERIDA'
        else: resultado = 'LIMINAR'
    marcas = []
    for k, v in MARCAS:
        if k in tl and v not in marcas and not (v == 'corrigido' and 'recorrigido' in marcas):
            marcas.append(v)
    if 'conforme parecer marcos' in tl and 'ajustado' not in marcas: marcas.append('ajustado')
    if t.startswith('#') or ' # ' in t: marcas.append('#')
    marcos = 'Marcos' in nomes or ' marcos ' in f' {tl} '
    nomes = ['Cecília' if n == 'Cecilia' else 'Márcia' if n == 'Marcia' else n for n in nomes]
    nomes_ass = [n for n in nomes if n != 'Marcos'] or (['Marcos'] if marcos_tmp(t) else [])
    # nível de prioridade (ordem das instruções do projeto)
    if pasta == 'OURO': nivel = 1
    elif CORRECAO & set(marcas): nivel = 2
    elif marcos: nivel = 3
    else: nivel = 4
    snip = x.get('contentSnippet', '') or ''
    ramo = ''
    r = re.search(r'(?:APELA[ÇC][ÃA]O C[ÍI]VEL|AGRAVO DE INSTRUMENTO|EMBARGOS DE DECLARA[ÇC][ÃA]O|REMESSA NECESS[ÁA]RIA|AGRAVO INTERNO|MANDADO DE SEGURAN[ÇC]A)\.\s*((?:DIREITO|PROCESSO)[^.]{3,80})\.', snip)
    if r: ramo = r.group(1).strip().title().replace(' E ', ' e ').replace(' Do ', ' do ').replace(' Da ', ' da ').replace(' De ', ' de ')
    corpo = snip
    k = min([p for p in (snip.find('EMENTA'), snip.find('RELATÓRIO')) if p >= 0] or [0])
    corpo = snip[k:k + 1500].lower().replace('distrito federal e dos territórios', '')
    base = f'{tl} {assunto.lower()} {corpo}'
    temas = sorted({re.sub(r'\D', '', n).lstrip('0') for n in re.findall(r'tema\s*(?:repetitivo\s*|de repercuss[aã]o geral\s*)?(?:n[º°.]?\s*)?(\d[\d.]{0,5})', base)} - {''}, key=int)
    mats = [nome for nome, pat in MATERIAS if re.search(pat, f'{tl} {assunto.lower()}')]
    if not mats:
        mats = [nome for nome, pat in MATERIAS if re.search(pat, base)][:2]
    ementa = ''
    e = re.search(r'EMENTA\s*\n+\s*([^\n]{20,400})', snip)
    if e: ementa = e.group(1).strip()
    return {
        'Nível': nivel, 'Pasta': f'{pasta}/{classe_pasta}', 'Classe': classe, 'Processo': proc,
        'Assessor': ', '.join(nomes_ass), 'Marcos': 'sim' if marcos else '', 'Resultado': resultado,
        'Marcadores': ', '.join(marcas), 'Tipo': tipo, 'Matéria': '; '.join(mats), 'Ramo (ementa)': ramo,
        'Temas': ', '.join(temas), 'Assunto (título)': assunto, 'Cabeçalho da ementa': ementa[:300],
        'Arquivo': x['title'], 'Link': f"https://drive.google.com/file/d/{x['id']}/view", 'ID': x['id'],
        'Enviado em': x['createdTime'][:10],
    }


if __name__ == '__main__':  # importável: atualizar-indice.py usa analisar()
    F = {}
    for g in sorted(glob.glob(os.environ.get('GDSXSR_BASE', '/home/claude/gdsxsr') + '/lst/ok/*.json')):
        for x in json.load(open(g))['files']:
            if x['id'] not in F or len(x.get('contentSnippet', '')) > len(F[x['id']].get('contentSnippet', '')):
                F[x['id']] = x
    linhas = [analisar(x) for x in F.values()]
    # duplicatas (mesmo processo + classe em mais de uma pasta)
    cont = collections.Counter((l['Classe'], l['Processo']) for l in linhas if l['Processo'])
    for l in linhas:
        l['Duplicado'] = 'sim' if l['Processo'] and cont[(l['Classe'], l['Processo'])] > 1 else ''
    linhas.sort(key=lambda l: (l['Classe'] != 'APC', l['Classe'] != 'AGI', l['Classe'], l['Nível'], l['Matéria'], l['Processo']))
    json.dump(linhas, open(os.environ.get('GDSXSR_BASE', '/home/claude/gdsxsr') + '/indice.json', 'w'), ensure_ascii=False, indent=0)
    print(len(linhas), 'linhas')
    print('nível', collections.Counter(l['Nível'] for l in linhas))
    print('classe', collections.Counter(l['Classe'] for l in linhas))
    print('resultado', collections.Counter(l['Resultado'] for l in linhas))
    print('assessor', collections.Counter(l['Assessor'] for l in linhas).most_common(25))
    print('sem matéria', sum(1 for l in linhas if not l['Matéria']), '| sem ramo', sum(1 for l in linhas if not l['Ramo (ementa)']))
    print('tipos', collections.Counter(l['Tipo'] for l in linhas))
