#!/usr/bin/env python3
"""Filtra claude/INDICE-MODELOS-GDSXSR.csv e imprime só os melhores modelos (nunca ler o CSV inteiro).

Uso: python3 buscar_modelos.py --classe APC [--resultado DPP] [--tipo voto] [--n 8] palavra ...
As palavras buscam (sem acento, sem caixa) em Matéria, Ramo, Temas e Assunto.
Ordem: Nível (1 OURO, 2 corrigido/alterado, 3 Marcos, 4 demais), depois nº de palavras casadas.
"""
import argparse, csv, pathlib, unicodedata

def n(s): return unicodedata.normalize("NFD", (s or "").lower()).encode("ascii", "ignore").decode()

ap = argparse.ArgumentParser()
ap.add_argument("palavras", nargs="*")
ap.add_argument("--classe"); ap.add_argument("--resultado"); ap.add_argument("--tipo", default="voto")
ap.add_argument("--n", type=int, default=8)
ap.add_argument("--csv", default=str(pathlib.Path(__file__).resolve().parents[1] / "INDICE-MODELOS-GDSXSR.csv"))
a = ap.parse_args()
pal = [n(p) for p in a.palavras]
linhas = []
for r in csv.DictReader(open(a.csv, encoding="utf-8-sig")):
    if a.classe and n(r["Classe"]) != n(a.classe): continue
    if a.tipo and n(r["Tipo"]) != n(a.tipo): continue
    if a.resultado and n(r["Resultado"]) != n(a.resultado): continue
    campo = n(" ".join(r[c] for c in ("Matéria", "Ramo (ementa)", "Temas", "Assunto (título)")))
    hit = sum(p in campo for p in pal)
    if pal and not hit: continue
    linhas.append((int(r["Nível"] or 4), -hit, r))
linhas.sort(key=lambda x: (x[0], x[1]))
for nv, h, r in linhas[:a.n]:
    print(f'N{nv} {r["Classe"]} {r["Processo"]} {r["Resultado"]} {r["Assessor"]} | {r["Assunto (título)"][:70]} | ID {r["ID"]}')
print(f"({len(linhas)} candidatos)")
