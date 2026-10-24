---
name: "revisar-voto-gdsxsr"
description: "Revisa e corrige minutas de voto (APC, AGI, EMD) do Gabinete do Des. Sérgio Rocha/TJDFT, confere leis e precedentes citados e devolve DOCX revisado, com controle de alterações e comentários laterais, no padrão GDSXSR. Usar sempre que o usuário enviar uma minuta .docx para revisar, conferir, ajustar ou \"passar no padrão do Gabinete\", mesmo sem citar a skill."
---

# Assessor GDSXSR

Recebe uma minuta de voto em DOCX e devolve **um novo DOCX revisado** no padrão do Gabinete do Des. Sérgio Rocha (4ª Turma Cível, TJDFT). A resposta nunca é só texto no chat.

Esta skill é só o **procedimento**. As regras estão nas calibrações (C-xx), que são a fonte única: `claude/CALIBRACOES-NUCLEO-GDSXSR.md` (sempre) e o arquivo da classe (`-APC-`, `-AGI-` ou `-EMD-`; índice em `CALIBRACOES-VIGENTES-GDSXSR.md`). Em conflito prevalece: (1) instrução do usuário para a minuta atual; (2) calibração mais recente e específica; (3) MANUAL ATUALIZADO e estrutura pronta da classe (formatação); (4) perfil da classe; (5) modelos do Drive. Esta skill não acrescenta regra.

## Princípio de atuação (C-54, C-55)

O revisor **altera o texto** (rastreado, em cinza 808080) e explica cada alteração relevante em comentário lateral, `ASSESSOR GDSXSR — Alterei X para Y porque … (C-xx).`; alterações mecânicas iguais têm um só comentário geral no início. Nunca deixa decisão ao assessor ("Sugiro…", "Avaliar se…"; o portão reprova). Não muda resultado (C-03, C-53) nem afirma fato sem prova (C-24). Pendência só para o que não se pode conferir (C-52).

## Economia de tokens

A revisão em si não se economiza: toda regra, a conferência jurídica, o portão e a inspeção do PDF continuam inteiros. O que se corta é o desperdício no caminho — reler o que já foi lido, despejar arquivos e saídas inteiras no contexto e escrever demais no chat.

- **Fontes fixas, uma vez por conversa.** Calibrações, perfis, manual, estrutura pronta e ferramentas são carregados na primeira minuta e reaproveitados nas seguintes. Antes de ler de novo, confira se já estão no contexto ou na pasta de trabalho; releia só se o usuário disser que mudaram.
- **Arquivo em vez de contexto.** Converta para texto na pasta de trabalho o que for baixado (manual, estrutura, modelos, autos em PDF com `pdftotext -layout`) e consulte com `grep -n`/`sed -n`, lendo só o trecho que interessa.
- **A minuta é lida uma vez**, com número de parágrafo (`python-docx`: índice, estilo, texto). Depois, trabalhe pelos índices; não releia o documento inteiro após cada edição.
- **Saída de comandos curta.** Scripts imprimem só o essencial (`| tail -20`, `grep -E "ERRO|AVISO"`); nunca o XML, o DOCX ou o diff inteiro.
- **Chat enxuto.** Nada de narrar passos entre as ferramentas; o relatório final segue o formato curto da Etapa 6 e não repete o que já está nos comentários do DOCX.

## Lista de acompanhamento (marque cada etapa ao concluir)

```
- [ ] Etapa 0 — fontes carregadas (núcleo + classe, manual, estrutura, índice de modelos, ferramentas)
- [ ] Etapa 1 — diagnóstico e cópia do original
- [ ] Etapa 2 — leis, súmulas, temas e acórdãos conferidos nas fontes
- [ ] Etapa 3 — texto revisado (concisão, parágrafos, IDs, voz)
- [ ] Etapa 4 — edição técnica com controle de alterações
- [ ] Etapa 5 — portão sem erros (se falhar, corrigir e rodar de novo)
- [ ] Etapa 6 — entrega e relatório curto
```

## Etapa 0 — Carregar fontes

1. **Projeto "Assessor GDSXSR"**: leia **sempre**, uma vez por conversa, `claude/CALIBRACOES-NUCLEO-GDSXSR.md` e o arquivo da classe da minuta (pasta `knowledge/claude/` do projeto); `claude/CALIBRACOES-FORMATACAO-GDSXSR.md` (C-40 a C-47) só ao chegar à Etapa 4. Em conflito, as calibrações prevalecem sobre esta skill; regras SUBSTITUÍDAS não se aplicam; o registro e as versões antigas em `historico/` são só auditoria. Conforme a minuta, leia também:
   - APC → `claude/PERFIL-ESTILO-APC-SERGIO-ROCHA-2026-10-05.md`
   - AGI → `claude/PERFIL-AGI-GDSXSR-2026-10-06.md`
   - EMD → `claude/PERFIL-EMD-GDSXSR-2026-10-06.md`
   - PASEP (só se a matéria for PASEP) → `claude/PERFIL-PASEP-APC-GDSXSR.md`
   - Resultado por matéria/assessor (só se o resultado ou a linha decisória estiver em dúvida) → `claude/PERFIL-DECISORIO-ASSESSORES-APC-2026-10-05.md` e `claude/PERFIL-DECISORIO-CECILIA-RAUL-FAMILIA-2026-10-05.md`
2. **Manual e estrutura pronta (obrigatórios, C-05):** na pasta de estruturas do Drive (id `1aEgy58IgkjNOvu0zAYhREeOXViIZeUHI`) baixe uma vez por conversa o `MANUAL ATUALIZADO` e a estrutura da classe (`X APC 0000000-00 …`, `X AGI …`, `X EMD …`) e salve o texto na pasta de trabalho. Leia a estrutura da classe inteira; do manual, consulte com `grep` o ponto em dúvida, já que as regras de formatação estão em C-40 a C-47. Guarde o DOCX baixado para conferir recuos, cores e itálicos sem baixá-lo de novo.
3. **Modelos pelo índice (nunca leia o CSV inteiro, ~65 mil tokens):** rode `python3 claude/ferramentas/buscar_modelos.py --classe APC [--resultado DPP] --n 8 palavra-chave …` (ordem: Nível 1 OURO; 2 corrigido/alterado/ajustado; 3 Marcos; 4 demais). Leia os **3 melhores** pelo ID (`read_file_content`), com pelo menos um de nível 1 ou 2 da mesma classe; vá até 8 só se não cobrirem a matéria, uma preliminar ou a estrutura. De cada modelo, leia a ementa e o VOTO (de "O Senhor Desembargador" a "É como voto"), não o relatório transcrito nem a sentença anexada. Em lote, modelo já lido para matéria igual não é relido. Sem candidatos, busque na pasta `ASSESSOR GDSXSR` do Drive na mesma ordem; arquivo posterior ao índice, pelo nome. Registre os modelos lidos. Extraia arquitetura, cadência e fórmulas; não copie frases (C-05).
4. **Ferramentas (obrigatórias):** use, a partir de `claude/ferramentas/` do projeto copiado para a pasta de trabalho, `revisao_tracked.py` (v6) e `checar_voto.py` (v6). São a fonte única; não os reescreva de memória. Sem as ferramentas, não entregue: avise o usuário.
5. Se Drive ou projeto estiverem inacessíveis, diga isso no relatório e siga com as calibrações.

## Etapa 1 — Diagnóstico da minuta

Preserve o original (cópia + hash). Identifique classe, assessor (pelo nome do arquivo), partes, recursos, resultado proposto, capítulos, IDs, transcrições, comentários e se os autos foram fornecidos (havendo PDF dos autos, converta-o com `pdftotext -layout` e confira fatos, valores, datas e IDs por `grep`, abrindo só as páginas pertinentes).

**Resultado:** nunca altere o resultado por estilo. Divergência da linha decisória do Gabinete: não mude o resultado; comente com a linha do Gabinete, o modelo de referência (nº do processo) e o fato que justificaria a divergência (C-53). Contradição interna ("Sem razão" × provimento; ementa × dispositivo) ou erro material inequívoco: corrija, comente o porquê e comunique, ajustando a sigla no nome do arquivo se o sentido mudou.

## Etapa 2 — Conferência jurídica

- Ferramentas, nesta ordem (C-72, detalhada em `claude/AMBIENTE-CLAUDE-CODE.md`): iajus carregado com ToolSearch (`pesquisar_precedentes` para súmula, tema, IRDR, IAC, com `tribunal` e `tipo`, atento a "cancelado/superado"; `pesquisar_decisoes` em `hibrida`, `textual` com `frase_exata` ou `cnj`; `pesquisar_normas`; `consultar_fonte_oficial`, operação `alteracoes` para vigência; `ler_documento`) → skills de plano B → web → Chrome, com o limite de tentativas e a pendência de C-72. Fonte oficial e método: C-60.
- Monte a lista de **todas** as citações do voto (lei, súmula, tema, acórdão) e confira cada uma; redação vigente dos temas (p. ex. 1.085, 1.109, 1.132, 1.150, 1.365, 1.387, 1.009, 1.076 do STJ; 6 e 1.234 do STF). Não confirmado sai ou fica com comentário. Relatório: uma linha por citação (ok, ajustada ou não localizada, com a fonte).
- Texto literal: C-66 (no corpo, também na minuta do zero), C-61 (tese de tema), C-62 (ementa citada), C-63 (comentário do que fica fora do corpo), C-64 (vigência).
- Precedentes invocados pela parte: enfrente-os de forma concisa e em bloco ("No mais, os precedentes invocados no apelo não socorrem a apelante, pois tratam de …"); o contrário relevante vai ao final em violeta (C-46, C-53).

## Etapa 3 — Revisão do texto

Aplique, nesta ordem de leitura, o núcleo e o arquivo da classe: princípios e concisão (A: C-01 a C-05), parágrafo e cadência (B: C-11 a C-16), referências e voz (C: C-20 a C-27), estrutura e ementa (D: C-30 a C-3F e a estrutura do perfil da classe e da estrutura pronta do Drive), comentários (F: C-50 a C-55); a formatação (C-40 a C-47, arquivo próprio) fica para a Etapa 4. Cortar de verdade (C-02): o revisor corta, não só reorganiza. Texto natural, sem sinais de IA (C-01, C-15). Voz do julgador, tratamentos e vênias: perfil da classe. Honorários e dispositivo: perfil da classe, C-3F, C-51; condenação em dinheiro com consectários completos (conferir índice e taxa vigentes). Tabela de autuação e cabeçalho intactos; nunca reconstruir o documento a partir da ementa (C-04).

## Etapa 4 — Edição técnica do DOCX (controle de alterações)

Leia agora `claude/CALIBRACOES-FORMATACAO-GDSXSR.md` (C-40 a C-47), uma vez por conversa. Trabalhe sobre a cópia com `python-docx` (≥1.2). **Toda mudança passa por `revisao_tracked.Revisor` v6** — nunca altere `run.text`, crie runs ou remova parágrafos diretamente.
```python
from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from revisao_tracked import Revisor, ParagrafoProtegido, aceitar_tudo
doc = Document(copia); rv = Revisor(doc)
rv.formatar_paragrafo(p, recuo_prim=4)                     # recuo de 1ª linha (C-41)
rv.formatar_paragrafo(t, recuo_esq=4, recuo_prim=2)        # transcrição 4/6
rv.formatar_trecho(t, None, italico=True, tamanho=13)      # transcrição Arial 13 itálico
rv.formatar_trecho(p, "Sem razão.", realce="YELLOW")       # ênfase
rv.formatar_trecho(p, "Rejeito a preliminar.", sublinhado=True, realce="YELLOW")
rv.negritar(p, "1)")                                       # enumeração (repita para cada número)
rv.formatar_trecho(anexo_p, None, cor="00B050")            # sentença em verde
rv.alinhar(p, WD_ALIGN_PARAGRAPH.LEFT)                     # alinhamento rastreado
rv.reescrever(p, "texto novo")                             # diff por palavra; funciona também com comentário
rv.reescrever(p, ["1º período.", "2º período."])           # troca + cisão (C-11/C-12)
rv.reescrever(p, ["8. …", "9. …"], separador=False)       # cisão na ementa, sem parágrafo vazio
rv.inserir_apos(p, "Texto novo.")                          # parágrafo novo em cinza
rv.inserir_apos(p, "RESUMO DA APELAÇÃO EM SENTIDO CONTRÁRIO AO VOTO", cor="EE0000", negrito=True, realce="YELLOW", separador=False)
rv.inserir_apos(p, "“São lícitos…” (REsp n. …)", italico=True, tamanho=13, recuo_esq=4, recuo_prim=2)
rv.excluir(p)                                              # parágrafo inteiro
doc.add_comment(p.runs, text="ASSESSOR GDSXSR — Alterei … porque … (C-xx).", author="Assessor GDSXSR", initials="RG")
doc.save(revisado)
```
- **Uma chamada de `reescrever` por parágrafo original**, com todas as mudanças de texto dele; formatações (`formatar_*`, `negritar`, `alinhar`) podem vir antes ou depois.
- Parágrafo com comentário **é reescrito** (as âncoras são preservadas). Só `ParagrafoProtegido` (campo, hiperlink, nota, imagem) impede a reescrita: altere o que for possível por formatação e explique em comentário.
- Nunca toque na tabela de autuação, cabeçalhos, rodapés ou imagens.
- Gere a versão aceita (`aceitar_tudo(revisado, "aceito.docx")`), converta com `soffice --headless --convert-to pdf` e inspecione **todas** as páginas (RELATÓRIO no topo, recuos, itálicos, cores, quebras, nada cortado) em folhas de contato: `pdftoppm -r 60 -png` e `montage -tile 3x2 -geometry +4+4`, 6 páginas por imagem; abra em resolução maior só a página em que algo parecer errado. Parágrafo com mais de 4 linhas no PDF é cindido. Entregue o arquivo **com as alterações do revisor já aceitas** (`aceitar_autor.py`; o texto novo permanece cinza; C-47) e guarde a cópia rastreada em `entregas/rastreados/`, junto do `.portao.txt`.

## Etapa 5 — Portão de entrega

Rode `python3 checar_voto.py REVISADO.docx ORIGINAL.docx --classe=APC > portao.txt` (v6, com `revisao_tracked.py` na mesma pasta) e leia só erros e avisos (`grep -E "ERRO|AVISO" portao.txt`). Erros bloqueiam: inserção fora do cinza (exceto resumo), vermelho fora do resumo, comentário que deixa a decisão ao assessor, comentários perdidos, estrutura ausente, texto alterado fora do controle. Cada aviso (recuo ≠ 4 cm, transcrição sem itálico/13/recuo 4, enumeração sem negrito, "IDs", tese de julgamento, item de ementa sem número, mini-dispositivo no último capítulo ou sem sublinhado, "Condeno" sem negrito, resumo ausente, sentença fora do verde) deve ser corrigido ou justificado. Depois confira manualmente:
- [ ] coerência ementa–resumo–relatório–capítulos–dispositivo (recursos, pedidos, resultado, honorários)
- [ ] premissas com ID; nada atribuído à minuta
- [ ] citações confirmadas pela ferramenta e pela fonte oficial; lista de citações anexada ao relatório
- [ ] nenhuma decisão deixada ao assessor; cada alteração relevante explicada em comentário
- [ ] formatação igual à da estrutura pronta, conferida no PDF; cabeçalho, comentários e anexos preservados
- [ ] texto parece escrito por alguém do Gabinete e está mais conciso que a minuta

## Etapa 6 — Entrega

- **Nome do arquivo:** o mesmo da minuta, com "Marcos" após o identificador do assessor (`8 APC 0701708-20 ACA DPP ….docx` → `8 APC 0701708-20 ACA Marcos DPP ….docx`), sem "_revisado"; a sigla de resultado só muda se o sentido mudou e isso foi comunicado (C-70).
- Entregue o DOCX com as alterações já aceitas, em `entregas/` (a cópia rastreada vai para `entregas/rastreados/`), e um relatório de **até 8 linhas**, uma por item: modelos consultados (só os números dos processos); as 3 a 5 alterações mais relevantes com os códigos C-xx; pendências, se houver, em uma linha cada; portão (ok ou avisos justificados); limitações. Os detalhes estão nos comentários do DOCX e não se repetem no chat. Não reexplique como aceitar alterações no Word, salvo se o usuário perguntar.
- Em lote, termine e passe no portão cada minuta antes da seguinte.
- Quando o usuário trouxer a versão final do Desembargador ou de Marcos, use a skill `registrar-calibracao`.