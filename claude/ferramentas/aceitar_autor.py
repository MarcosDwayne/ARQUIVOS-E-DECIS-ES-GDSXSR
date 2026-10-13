"""Aceita apenas as alterações rastreadas de um autor (Revisor GDSXSR); preserva as de terceiros e os comentários."""
import sys
from docx import Document
from docx.oxml.ns import qn
W = lambda t: qn("w:" + t)
def meu(e, autor): return e.get(W("author")) == autor
def aceitar(entrada, saida, autor="Revisor GDSXSR"):
    d = Document(entrada); body = d.element.body
    for x in list(body.iter(W("del"))):
        par = x.getparent()
        if par is not None and par.tag != W("rPr") and meu(x, autor): par.remove(x)
    for x in list(body.iter(W("ins"))):
        par = x.getparent()
        if par is not None and par.tag != W("rPr") and meu(x, autor):
            i = par.index(x)
            for c in list(x): par.insert(i, c); i += 1
            par.remove(x)
    for tag in ("pPrChange", "rPrChange"):
        for e in list(body.iter(W(tag))):
            if meu(e, autor): e.getparent().remove(e)
    for p in list(body.iter(W("p"))):
        rpr = p.find(W("pPr") + "/" + W("rPr"))
        if rpr is None: continue
        for i in rpr.findall(W("ins")):
            if meu(i, autor): rpr.remove(i)
        dl = rpr.find(W("del"))
        if dl is not None and meu(dl, autor):
            rpr.remove(dl)
            nxt = p.getnext()
            if nxt is not None and nxt.tag == W("p"):
                pos = 1 if nxt.find(W("pPr")) is not None else 0
                for c in [c for c in p if c.tag != W("pPr")]: nxt.insert(pos, c); pos += 1
            p.getparent().remove(p)
    d.save(saida)
if __name__ == "__main__":
    aceitar(sys.argv[1], sys.argv[2])
