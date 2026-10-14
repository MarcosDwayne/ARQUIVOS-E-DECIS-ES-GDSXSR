#!/usr/bin/env python3
"""Roda portão e comparação com a versão final em cada caso de avaliacoes/casos.json.
Uso: python3 avaliacoes/avaliar.py   (cada caso: pasta em avaliacoes/casos/NOME com agente.docx e final.docx)"""
import json, os, subprocess, sys
RAIZ = os.path.dirname(os.path.abspath(__file__))
FERR = os.path.join(RAIZ, "..", "claude", "ferramentas")

def rodar(args):
    r = subprocess.run([sys.executable] + args, capture_output=True, text=True)
    return (r.stdout + r.stderr).strip().splitlines()

casos = json.load(open(os.path.join(RAIZ, "casos.json"), encoding="utf8")).get("casos", [])
if not casos:
    print("Nenhum caso cadastrado em avaliacoes/casos.json (veja README.md)."); sys.exit(0)
for c in casos:
    pasta = os.path.join(RAIZ, "casos", c["nome"])
    ag, fin = os.path.join(pasta, "agente.docx"), os.path.join(pasta, "final.docx")
    print(f"=== {c['nome']} ({c.get('classe','APC')})")
    faltando = [f for f in (ag, fin) if not os.path.exists(f)]
    if faltando:
        print("  arquivos ausentes:", ", ".join(os.path.basename(f) for f in faltando)); continue
    portao = rodar([os.path.join(FERR, "checar_voto.py"), ag, os.path.join(pasta, "original.docx"), f"--classe={c.get('classe','APC')}"])
    print("  portão:", sum("[ERRO" in l for l in portao), "erro(s),", sum("[AVISO" in l for l in portao), "aviso(s)")
    for l in rodar([os.path.join(FERR, "comparar_versoes.py"), ag, fin])[:12]:
        print("  ", l)
