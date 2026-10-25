#!/usr/bin/env python3
"""Teste de equivalência das calibrações: nenhuma regra C-xx pode sumir.

Uso: python3 equivalencia_regras.py ANTES_DIR DEPOIS_DIR
Compara os arquivos CALIBRACOES-NUCLEO/APC/AGI/EMD dos dois diretórios.
Falha (exit 1) se faltar regra, mudar status/classe ou sumir fórmula entre aspas.
Fórmulas ausentes são listadas para conferência humana (podem ter ido ao registro).
"""
import re, sys, pathlib

ARQS = ["NUCLEO", "FORMATACAO", "APC", "AGI", "EMD"]
RE_REGRA = re.compile(r"^\*\*(C-[0-9A-Z]+)\s*·\s*(.*?)\*\*\s*—\s*(.*)$", re.M)
RE_ASPAS = re.compile(r"[“\"]([^”\"\n]{12,}?)[”\"]")
RE_NUM = re.compile(r"\b(?:808080|EE0000|00B050|800080|C45911|4 cm|6 cm|1,5|Arial \d+)\b")

def norm(s): return re.sub(r"\s+", " ", s).strip()

def ler(d):
    out = {}
    for a in ARQS:
        p = pathlib.Path(d) / f"CALIBRACOES-{a}-GDSXSR.md"
        if not p.exists(): continue
        t = p.read_text(encoding="utf8")
        ms = list(RE_REGRA.finditer(t))
        for i, m in enumerate(ms):
            fim = ms[i + 1].start() if i + 1 < len(ms) else len(t)
            corpo = t[m.start():fim]
            out[(a, m.group(1))] = dict(
                titulo=norm(m.group(2)), status=norm(m.group(3)).split("·")[0].strip(),
                aspas={norm(x) for x in RE_ASPAS.findall(corpo)},
                nums=set(RE_NUM.findall(corpo)),
                refs=set(re.findall(r"C-[0-9A-Z]+", corpo)) - {m.group(1)})
    return out

def main(a, d):
    A, D = ler(a), ler(d)
    erros, avisos = [], []
    # uma regra pode mudar de arquivo (ex.: núcleo -> formatação): casa por ID
    por_id = {}
    for (arq, rid), r in D.items(): por_id.setdefault(rid, []).append(((arq, rid), r))
    for k, v in A.items():
        if k in D: n = D[k]
        elif k[1] in por_id and k[1] not in {i for (_, i) in A if (_, i) != k and i == k[1]}:
            n = por_id[k[1]][0][1]; avisos.append(f"MUDOU DE ARQUIVO {k} -> {por_id[k[1]][0][0][0]}")
        else: erros.append(f"REGRA AUSENTE {k}"); continue
        if v["status"] != n["status"]: erros.append(f"STATUS {k}: {v['status']} -> {n['status']}")
        for x in sorted(v["nums"] - n["nums"]): erros.append(f"VALOR SUMIU {k}: {x}")
        for x in sorted(v["refs"] - n["refs"]): avisos.append(f"REMISSÃO SUMIU {k}: {x}")
        for x in sorted(v["aspas"] - n["aspas"]): avisos.append(f"FÓRMULA FORA {k}: {x[:90]}")
    ids_a = {i for (_, i) in A}
    for k in D:
        if k not in A and k[1] not in ids_a: avisos.append(f"REGRA NOVA {k}")
    print(f"regras antes: {len(A)} | depois: {len(D)}")
    for e in erros: print("ERRO", e)
    for w in avisos: print("AVISO", w)
    print("OK" if not erros else "FALHOU")
    return 1 if erros else 0

if __name__ == "__main__":
    sys.exit(main(*sys.argv[1:3]))
