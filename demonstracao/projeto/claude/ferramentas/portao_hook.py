#!/usr/bin/env python3
"""Hook Stop: roda o portão (checar_voto.py) nas minutas de entregas/ ainda sem .portao.txt atualizado.
Erros do portão voltam ao Claude (exit 2) para correção; avisos só ficam no .portao.txt."""
import json, os, re, subprocess, sys, glob
try:
    ev = json.load(sys.stdin)
except Exception:
    ev = {}
if ev.get("stop_hook_active"):
    sys.exit(0)
raiz = os.environ.get("CLAUDE_PROJECT_DIR") or os.getcwd()
ferr = os.path.join(raiz, "claude", "ferramentas", "checar_voto.py")
if not os.path.exists(ferr):
    sys.exit(0)
erros_total = []
for docx in glob.glob(os.path.join(raiz, "entregas", "rastreados", "*.docx")):
    if os.path.basename(docx).startswith("~$"):
        continue
    saida = docx[:-5] + ".portao.txt"
    if os.path.exists(saida) and os.path.getmtime(saida) >= os.path.getmtime(docx):
        continue
    m = re.search(r"\b(APC|AGI|EMD)\b", os.path.basename(docx))
    r = subprocess.run([sys.executable, ferr, docx, f"--classe={m.group(1) if m else 'APC'}"],
                       capture_output=True, text=True)
    open(saida, "w", encoding="utf-8").write(r.stdout + r.stderr)
    erros = [l for l in r.stdout.splitlines() if l.startswith("[ERRO]")]
    if erros:
        erros_total.append(f"{os.path.basename(docx)}: " + " | ".join(erros[:5]))
if erros_total:
    print("Portão GDSXSR reprovou a entrega. Corrija e rode de novo:\n" + "\n".join(erros_total), file=sys.stderr)
    sys.exit(2)
