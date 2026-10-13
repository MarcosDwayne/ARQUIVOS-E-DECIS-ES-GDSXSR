#!/usr/bin/env python3
"""OCR de PDFs formados por imagens (Revisor GDSXSR).

Gera um .txt com o texto de cada página, marcando o número da página do PDF e,
quando achar o rodapé do PJe ("Num. 88669555 - Pág. 18"), o ID da peça.

Uso:
  python3 ocr_pdf.py ARQUIVO.pdf                      # PDF inteiro
  python3 ocr_pdf.py ARQUIVO.pdf --paginas 1-50       # só um intervalo (ex.: 1-50,120,300-310)
  python3 ocr_pdf.py ARQUIVO.pdf --saida saida.txt --jobs 4 --dpi 200

É retomável: cada página pronta fica em <saida>.partes/; ao rodar de novo só
faltam as que ainda não foram feitas. Páginas que já têm texto digital são
aproveitadas sem OCR (use --forcar-ocr para refazer tudo por imagem).
Requer: pdftoppm, pdftotext (poppler) e tesseract com idioma "por".
"""
import argparse, os, re, shutil, subprocess, sys, tempfile, time
from concurrent.futures import ProcessPoolExecutor

RE_NUM = re.compile(r"Num\.?\s*(\d{7,9})\s*[-–—]\s*P[áa]g\.?\s*(\d+)", re.I)
MIN_CHARS_TEXTO = 40  # abaixo disso a página é tratada como imagem


def num_paginas(pdf):
    out = subprocess.run(["pdfinfo", pdf], capture_output=True, text=True).stdout
    m = re.search(r"^Pages:\s+(\d+)", out, re.M)
    if not m:
        sys.exit("Não consegui ler o PDF (pdfinfo falhou).")
    return int(m.group(1))


def parse_intervalo(s, total):
    if not s:
        return list(range(1, total + 1))
    pgs = set()
    for parte in s.split(","):
        parte = parte.strip()
        if "-" in parte:
            a, b = parte.split("-", 1)
            pgs.update(range(int(a or 1), int(b or total) + 1))
        elif parte:
            pgs.add(int(parte))
    return sorted(p for p in pgs if 1 <= p <= total)


def processa(args):
    pdf, p, lang, dpi, forcar, partes = args
    destino = os.path.join(partes, f"p{p:05d}.txt")
    t0 = time.time()
    texto, metodo = "", "OCR"
    if not forcar:
        texto = subprocess.run(["pdftotext", "-layout", "-f", str(p), "-l", str(p), pdf, "-"],
                               capture_output=True, text=True, errors="ignore").stdout
        if len(texto.strip()) >= MIN_CHARS_TEXTO:
            metodo = "texto digital"
        else:
            texto = ""
    if not texto:
        with tempfile.TemporaryDirectory() as tmp:
            base = os.path.join(tmp, "pg")
            subprocess.run(["pdftoppm", "-r", str(dpi), "-gray", "-png", "-f", str(p), "-l", str(p),
                            "-singlefile", pdf, base], capture_output=True)
            img = base + ".png"
            if not os.path.exists(img):
                texto, metodo = "[ERRO: não foi possível converter a página em imagem]", "ERRO"
            else:
                r = subprocess.run(["tesseract", img, "stdout", "-l", lang, "--psm", "1",
                                    "-c", "preserve_interword_spaces=1"],
                                   capture_output=True, text=True, errors="ignore",
                                   env={**os.environ, "OMP_THREAD_LIMIT": "1"})
                texto = r.stdout
                if r.returncode != 0:
                    texto, metodo = f"[ERRO no tesseract: {r.stderr.strip()[:200]}]", "ERRO"
    seg = time.time() - t0
    m = RE_NUM.search(texto)
    cab = f"PÁGINA {p} (PDF)"
    if m:
        cab += f" | ID {m.group(1)} | Pág. {m.group(2)} da peça"
    cab += f" | {metodo}"
    with open(destino + ".tmp", "w", encoding="utf-8") as f:
        f.write(f"===== {cab} =====\n{texto.strip()}\n")
    os.replace(destino + ".tmp", destino)
    return p, seg, metodo


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("pdf")
    ap.add_argument("--saida", help="arquivo .txt de saída (padrão: ao lado do PDF)")
    ap.add_argument("--paginas", help="intervalo, ex.: 1-50,120,300-310 (padrão: todas)")
    ap.add_argument("--lang", default="por")
    ap.add_argument("--dpi", type=int, default=200)
    ap.add_argument("--jobs", type=int, default=os.cpu_count() or 2)
    ap.add_argument("--forcar-ocr", action="store_true", help="faz OCR mesmo onde há texto digital")
    ap.add_argument("--refazer", action="store_true", help="ignora páginas já prontas")
    a = ap.parse_args()

    for exe in ("pdftoppm", "pdftotext", "pdfinfo", "tesseract"):
        if not shutil.which(exe):
            sys.exit(f"Falta o programa '{exe}'. Veja a skill ocr-pdf-gdsxsr (instalação).")
    saida = a.saida or os.path.splitext(a.pdf)[0] + ".ocr.txt"
    partes = saida + ".partes"
    os.makedirs(partes, exist_ok=True)
    total = num_paginas(a.pdf)
    alvo = parse_intervalo(a.paginas, total)
    falta = [p for p in alvo if a.refazer or not os.path.exists(os.path.join(partes, f"p{p:05d}.txt"))]
    print(f"PDF com {total} páginas; pedidas {len(alvo)}; a processar agora {len(falta)}.", flush=True)

    t0, feitas, tempos = time.time(), 0, []
    if falta:
        with ProcessPoolExecutor(a.jobs) as ex:
            for p, seg, metodo in ex.map(processa, [(a.pdf, p, a.lang, a.dpi, a.forcar_ocr, partes) for p in falta]):
                feitas += 1
                if metodo == "OCR":
                    tempos.append(seg)
                if feitas % 10 == 0 or feitas == len(falta):
                    dec = time.time() - t0
                    print(f"  {feitas}/{len(falta)} ({dec:.0f}s, {dec/feitas:.1f}s/página em conjunto)", flush=True)
    if tempos:
        print(f"OCR: média {sum(tempos)/len(tempos):.1f}s por página em cada processo "
              f"({len(tempos)} páginas por imagem).")

    # junta tudo o que existe, em ordem de página
    prontas = sorted(f for f in os.listdir(partes) if re.fullmatch(r"p\d{5}\.txt", f))
    with open(saida, "w", encoding="utf-8") as out:
        for f in prontas:
            out.write(open(os.path.join(partes, f), encoding="utf-8").read() + "\n")
    print(f"Texto salvo em: {saida} ({len(prontas)} páginas prontas de {total}).")
    erros = [f for f in prontas if "| ERRO" in open(os.path.join(partes, f), encoding="utf-8").readline()]
    if erros:
        print(f"ATENÇÃO: {len(erros)} página(s) com erro: {', '.join(e[1:6].lstrip('0') for e in erros)}")


if __name__ == "__main__":
    main()
