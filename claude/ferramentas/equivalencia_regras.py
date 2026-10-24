#!/usr/bin/env python3
"""Teste de equivalência das calibrações: nenhuma regra C-xx pode sumir.

Uso: python3 equivalencia_regras.py ANTES_DIR DEPOIS_DIR
Compara os arquivos CALIBRACOES-NUCLEO/APC/AGI/EMD dos dois diretórios.
Falha (exit 1) se faltar regra, mudar status/classe ou sumir fórmula entre aspas.
Fórmulas ausentes são listadas para conferência humana (podem ter ido ao registro).
"""
import re, sys, pathlib

ARQS = ["NUCLEO", "APC", "AGI", "EMD"]
RE_REGRA = re.compile(r"^\*\*(C-[0-9A-Z]+)\s*·\s*(.*?)\*\*\s*—\s*(.*)$", re.M)
RE_ASPAS = re.compile(r"[“\"]([^”\"\n]{12,}?)[”\"]")
RE_NUM = re.compile(r"\b(?:808080|EE0000|00B050|800080|C45911|4 cm|6 cm|1,5|Arial \d+)\b")

def norm(s): return re.sub(r"\s+", " ", s).strip()

def ler(d):
    out = {}
    for a in ARQS:
        p = pathlib.Path(d) / f"CALIBRACOES-{a}-GDSXSR.md"
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
    for k, v in A.items():
        if k not in D: erros.append(f"REGRA AUSENTE {k}"); continue
        n = D[k]
        if v["status"] != n["status"]: erros.append(f"STATUS {k}: {v['status']} -> {n['status']}")
        for x in sorted(v["nums"] - n["nums"]): erros.append(f"VALOR SUMIU {k}: {x}")
        for x in sorted(v["refs"] - n["refs"]): avisos.append(f"REMISSÃO SUMIU {k}: {x}")
        for x in sorted(v["aspas"] - n["aspas"]): avisos.append(f"FÓRMULA FORA {k}: {x[:90]}")
    for k in D:
        if k not in A: avisos.append(f"REGRA NOVA {k}")
    print(f"regras antes: {len(A)} | depois: {len(D)}")
    for e in erros: print("ERRO", e)
    for w in avisos: print("AVISO", w)
    print("OK" if not erros else "FALHOU")
    return 1 if erros else 0

if __name__ == "__main__":
    sys.exit(main(*sys.argv[1:3]))
