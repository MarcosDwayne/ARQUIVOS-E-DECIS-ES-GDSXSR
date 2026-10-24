---
name: "ocr-pdf-gdsxsr"
description: "Faz OCR de PDFs de processo formados por imagens (sem texto selecionável) e gera .txt com página e ID da peça. Usar quando o PDF não tiver camada de texto."
---

# Leitura de PDFs do Assessor GDSXSR (MarkItDown + OCR)

## Regra de escolha
- **PDF com camada de texto → MarkItDown** (rápido, gera Markdown limpo).
- **PDF só imagem, ou páginas escaneadas dentro de PDF de texto → OCR** com `claude/ferramentas/ocr_pdf.py`, que marca a página do PDF e o ID da peça.
- **Para citar página do PDF ou ID da peça, use o `ocr_pdf.py`.** Ele aproveita o texto digital das páginas que têm e faz OCR nas que não têm. O MarkItDown não marca página.

## Armadilha: o teste simples de texto engana
Nos PDFs do PJe, toda página escaneada traz um carimbo digital ("Este documento foi gerado pelo usuário… Num. 80846476 - Pág. 1"). Por isso `pdftotext | wc -c` dá centenas de caracteres mesmo em página que é só imagem. Teste por página: pegue 2 ou 3 páginas do corpo da peça (não só a primeira) e veja se aparece o conteúdo, não só o carimbo. Se só aparece o carimbo, é imagem: OCR.

## MarkItDown (testado em 08/10/2026, versão 0.1.7)
Instalar (a nuvem começa limpa a cada sessão):
```
python3 -m pip install 'markitdown[pdf]'
```
Uso: `python3 -I -c "from markitdown import MarkItDown; print(MarkItDown().convert('arq.pdf').text_content)" > arq.md`

Resultado medido nos PDFs do projeto:
- AGI 0739606-17 (797 págs, todas com texto; os dois arquivos "AGI 0739606-17" são idênticos): converteu em ~103 s, 1,57 milhão de caracteres. Os 1.363 rodapés "Num. NNNNNNNN - Pág. N" ficaram no texto (como linhas de tabela), então o ID da peça sobrevive. O número da página do PDF não é marcado (não há separador entre páginas).
- Processo 0001746-54 (2.108 págs): o arquivo inteiro **falhou** (erro de fonte `PSSyntaxError` do pdfminer). Dividido em blocos de 200 páginas (com pypdf), 10 de 11 blocos converteram em 8 a 17 s cada; o último (págs. 2.001 a 2.108) falhou pelo mesmo erro. Se um bloco falhar, use `ocr_pdf.py` ou `pdftotext -layout` nele.
- Páginas escaneadas (testadas as págs. 1.825 a 1.827 do processo): o MarkItDown devolveu **só o carimbo do PJe** (1.325 caracteres para 3 páginas) e perdeu todo o corpo da peça, sem aviso. Ele não faz OCR.

O que o MarkItDown perde: o número da página do PDF; a separação entre peças; o texto de páginas-imagem. O ID da peça só aparece como rodapé em tabela.

`pdfseparate` corrompe o PDF desse processo; para cortar páginas use `pypdf` (`PdfWriter.add_page`).

## OCR
Ferramenta: `claude/ferramentas/ocr_pdf.py` (em /mnt/project-files/knowledge/claude/ferramentas/). Usa poppler + tesseract em português. Saída: um .txt em que cada página começa com
`===== PÁGINA 12 (PDF) | ID 88669555 | Pág. 18 da peça | OCR =====`.
O ID vem do rodapé do PJe ("Num. 88669555 - Pág. 18"); se o OCR não achar o rodapé, o cabeçalho traz só a página do PDF — confira na imagem antes de citar ID.

### Preparar o ambiente (a nuvem começa limpa a cada sessão)
```
which tesseract || (apt-get update && apt-get install -y tesseract-ocr tesseract-ocr-por)
```
poppler (pdftoppm, pdftotext, pdfinfo) já vem instalado. O script só usa a biblioteca padrão do Python.

### Como rodar
```
python3 ocr_pdf.py ARQUIVO.pdf                    # inteiro
python3 ocr_pdf.py ARQUIVO.pdf --paginas 1-50     # intervalo (aceita 1-50,120,300-310)
```
Opções: `--saida`, `--jobs` (padrão: núcleos), `--dpi` (200), `--forcar-ocr`, `--refazer`.

- **Retomável:** cada página pronta fica em `<saida>.partes/`; rodar de novo só faz o que falta. Se cair no meio, rode o mesmo comando.
- Páginas que já têm texto digital são aproveitadas sem OCR (marcadas "texto digital"). O corte é de 40 caracteres por página; como o carimbo do PJe sozinho pode passar disso, se uma página escaneada sair marcada "texto digital" só com o carimbo, refaça com `--forcar-ocr --paginas N`.
- O .txt final reúne tudo que já está pronto, não só o intervalo pedido.
- **Tempo medido** (4 núcleos): ~1,7 s/página no conjunto (~6 s por página em cada processo). Estime ~25 min para 800 páginas e ~1 h para 2.000. Para PDFs grandes, rode em segundo plano (`run_in_background`) e em blocos (`--paginas`), começando pelas peças que importam.

## Boas práticas
- Economize tokens: não leia o texto inteiro; use `grep -n` e leia só as páginas necessárias.
- OCR erra (acertou ~97% das palavras no teste): números de processo, valores, datas e IDs devem ser conferidos na imagem da página (`pdftoppm -r 100 -png -f N -l N`) antes de entrar no voto.
- Salve os arquivos de saída em trabalho/ ou /mnt/project-files/, nunca sobrescreva o PDF original.
- Antes de alterar esta skill ou as ferramentas, copie o arquivo para historico/backup-AAAA-MM-DD/.