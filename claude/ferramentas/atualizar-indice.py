#!/usr/bin/env python3
"""Acrescenta/atualiza linhas em claude/INDICE-MODELOS-GDSXSR.csv a partir de listagens do Drive, sem refazer o índice inteiro.

Uso: python3 atualizar-indice.py listagem1.json [listagem2.json ...]
Cada JSON é uma lista de arquivos (ou {"files": [...]}) com id, title, parentId, createdTime e, se houver, contentSnippet.
A classificação vem de analisar() em indexar-modelos.py (a pasta é reconhecida pelo parentId em PASTA).
Linha existente com o mesmo ID, ou com a mesma Pasta + Classe + Processo (arquivo reenviado com novo ID), é substituída;
as demais são acrescentadas. Imprime o que mudou.
"""
import csv, importlib.util, json, pathlib, sys

AQUI = pathlib.Path(__file__).resolve().parent
CSV = AQUI.parent / "INDICE-MODELOS-GDSXSR.csv"
spec = importlib.util.spec_from_file_location("indexar", AQUI / "indexar-modelos.py")
ix = importlib.util.module_from_spec(spec); spec.loader.exec_module(ix)

arquivos = {}
for g in sys.argv[1:]:
    d = json.load(open(g, encoding="utf-8"))
    for x in (d["files"] if isinstance(d, dict) else d):
        if x["parentId"] in ix.PASTA:
            arquivos[x["id"]] = x

with open(CSV, encoding="utf-8-sig", newline="") as f:
    leitor = csv.DictReader(f); cols = leitor.fieldnames; linhas = list(leitor)

subst = novas = 0
lote = set(arquivos)
for x in arquivos.values():
    r = ix.analisar(x)
    nova = {c: str(r.get(c, "")) for c in cols}
    chave = (nova["Pasta"], nova["Classe"], nova["Processo"])
    # substitui a linha do mesmo ID ou a versão antiga (outro ID, fora desta listagem) do mesmo processo; arquivos do mesmo
    # processo que chegam juntos (ex.: duas liminares) ficam como linhas separadas
    alvo = [i for i, l in enumerate(linhas) if l["ID"] == nova["ID"] or (nova["Processo"] and l["ID"] not in lote and (l["Pasta"], l["Classe"], l["Processo"]) == chave)]
    if alvo:
        linhas[alvo[0]] = nova; subst += 1
        for i in reversed(alvo[1:]): del linhas[i]
    else:
        linhas.append(nova); novas += 1

ordem = {"APC": 0, "AGI": 1}
linhas.sort(key=lambda l: (ordem.get(l["Classe"], 2), l["Classe"], int(l["Nível"] or 4), l["Matéria"], l["Processo"]))
with open(CSV, "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=cols); w.writeheader(); w.writerows(linhas)
print(f"{novas} linhas novas, {subst} substituídas, {len(linhas)} no total")
