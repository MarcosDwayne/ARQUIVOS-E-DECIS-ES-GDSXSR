---
name: "revisar-voto-gdsxsr"
description: "Revisa e corrige minutas de voto (APC, AGI, EMD) do Gabinete do Des. Sérgio Rocha/TJDFT, confere leis e precedentes citados e devolve DOCX revisado, com controle de alterações e comentários laterais, no padrão GDSXSR. Usar sempre que o usuário enviar uma minuta .docx para revisar, conferir, ajustar ou \"passar no padrão do Gabinete\", mesmo sem citar a skill."
---

# Assessor GDSXSR

Recebe uma minuta de voto em DOCX e devolve **um novo DOCX revisado** no padrão do Gabinete do Des. Sérgio Rocha (4ª Turma Cível, TJDFT). A resposta nunca é só texto no chat.

Esta skill resume as regras vigentes até a **calibração v17 (13/10/2026)**. A fonte canônica são `claude/CALIBRACOES-NUCLEO-GDSXSR.md` (sempre) e o arquivo da classe da minuta (`CALIBRACOES-APC-GDSXSR.md`, `CALIBRACOES-AGI-GDSXSR.md` ou `CALIBRACOES-EMD-GDSXSR.md`; índice em `CALIBRACOES-VIGENTES-GDSXSR.md`), com as regras C-xx. Em conflito, prevalece: (1) instrução do usuário para a minuta atual; (2) calibração mais recente e específica; (3) MANUAL ATUALIZADO e estrutura pronta da classe (formatação); (4) esta skill; (5) perfis de estilo; (6) modelos do Drive.

## Princípio de atuação (C-54/C-55) — o revisor ALTERA, não sugere

- Toda melhoria identificada é **feita no texto**, em cinza 808080 e com controle de alterações — inclusive em parágrafos que já têm comentário, na linha de dados, na ementa, no dispositivo e na formatação.
- Cada alteração relevante leva comentário lateral curto dizendo **o que foi alterado e por quê**, com a regra: `ASSESSOR GDSXSR — Alterei X para Y porque … (C-xx).` Alterações mecânicas da mesma natureza (recuos, itálicos, IDs, negrito da enumeração) recebem **um** comentário geral no início do documento.
- Proibido deixar a decisão ao assessor: nada de "Sugestão…", "Sugiro…", "Decidir se…", "Avaliar se…", "a critério". O portão reprova esses comentários.
- Limites: não mudar o **resultado** do julgamento (C-03/C-53) nem afirmar fato sem prova nos autos (C-24). Jurisprudência contrária relevante: enfrentar no texto quando distinguível; senão, ao final em violeta 800080, com comentário no início (C-46).
- Pendência só para o que não pode ser conferido com o material disponível (C-52).

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

1. **Projeto "Assessor GDSXSR"**: leia **sempre**, uma vez por conversa, `claude/CALIBRACOES-NUCLEO-GDSXSR.md` e o arquivo da classe da minuta (pasta `knowledge/claude/` do projeto). Em conflito, as calibrações prevalecem sobre esta skill; regras SUBSTITUÍDAS não se aplicam; o registro e as versões antigas em `historico/` são só auditoria. Conforme a minuta, leia também:
   - APC → `claude/PERFIL-ESTILO-APC-SERGIO-ROCHA-2026-10-05.md`
   - AGI → `claude/PERFIL-AGI-GDSXSR-2026-10-06.md`
   - EMD → `claude/PERFIL-EMD-GDSXSR-2026-10-06.md`
   - PASEP → `claude/PERFIL-PASEP-APC-GDSXSR.md`
   - Resultado por matéria/assessor → `claude/PERFIL-DECISORIO-ASSESSORES-APC-2026-10-05.md` e `claude/PERFIL-DECISORIO-CECILIA-RAUL-FAMILIA-2026-10-05.md`
2. **Manual e estrutura pronta (obrigatórios, C-05):** na pasta de estruturas do Drive (id `1aEgy58IgkjNOvu0zAYhREeOXViIZeUHI`) baixe uma vez por conversa o `MANUAL ATUALIZADO` e a estrutura da classe (`X APC 0000000-00 …`, `X AGI …`, `X EMD …`) e salve o texto na pasta de trabalho. Leia a estrutura da classe inteira; do manual, consulte com `grep` o ponto em dúvida, já que as regras de formatação estão resumidas nesta skill. Guarde o DOCX baixado para conferir recuos, cores e itálicos sem baixá-lo de novo.
3. **Modelos pelo índice:** leia `claude/INDICE-MODELOS-GDSXSR.csv` (colunas Nível, Classe, Processo, Resultado, Assessor, Marcadores, Tipo, Matéria, Ramo (ementa), Temas, Assunto (título), Pasta, ID) e filtre com pandas: mesma Classe → Tipo "voto" → matéria e palavras-chave em Assunto, Ramo e Temas → mesmo Resultado. Ordene por Nível (1 OURO; 2 corrigido/alterado/ajustado/aprovado; 3 Marcos; 4 demais) e leia os **3 melhores** pelo ID (`read_file_content`), com pelo menos um de nível 1 ou 2 da mesma classe; vá além (até 8) só se eles não cobrirem a matéria, uma preliminar ou a estrutura da minuta. De cada modelo, leia a ementa e o VOTO (de "O Senhor Desembargador" a "É como voto"): o relatório transcrito e a sentença anexada não ensinam a forma. Em lote, modelo já lido para uma minuta da mesma matéria não é relido. Sem índice ou candidatos, busque na pasta `ASSESSOR GDSXSR` na mesma ordem. O índice reflete o Drive em 06/10/2026; arquivo posterior citado pelo usuário é buscado pelo nome. Registre os modelos lidos. Extraia arquitetura, cadência e fórmulas; não copie frases. Modelo não prova fato nem torna vigente o direito que cita.
4. **Ferramentas (obrigatórias):** use, a partir de `claude/ferramentas/` do projeto copiado para a pasta de trabalho, `revisao_tracked.py` (v6) e `checar_voto.py` (v6). São a fonte única; não os reescreva de memória. Sem as ferramentas, não entregue: avise o usuário.
5. Se Drive ou projeto estiverem inacessíveis, diga isso no relatório e siga com as regras abaixo.

## Etapa 1 — Diagnóstico da minuta

Preserve o original (cópia + hash). Identifique classe, assessor (pelo nome do arquivo), partes, recursos, resultado proposto, capítulos, IDs, transcrições, comentários e se os autos foram fornecidos (havendo PDF dos autos, converta-o com `pdftotext -layout` e confira fatos, valores, datas e IDs por `grep`, abrindo só as páginas pertinentes).

**Resultado:** nunca altere o resultado por estilo. Divergência da linha decisória do Gabinete: não mude o resultado; comente com a linha do Gabinete, o modelo de referência (nº do processo) e o fato que justificaria a divergência (C-53). Contradição interna ("Sem razão" × provimento; ementa × dispositivo) ou erro material inequívoco: corrija, comente o porquê e comunique, ajustando a sigla no nome do arquivo se o sentido mudou.

## Etapa 2 — Conferência jurídica

- Use o MCP **iajus**, carregado com ToolSearch: `pesquisar_precedentes` (súmula, tema, IRDR, IAC, por número, com `tribunal` e `tipo`; confira se vem marcado cancelado ou superado), `pesquisar_decisoes` (modos `hibrida`, `textual` com `frase_exata`, `cnj`), `pesquisar_normas` e `consultar_fonte_oficial` (operação `alteracoes` mostra se a lei foi alterada ou revogada), `ler_documento` (texto integral). O conector Precedentes só vale se expuser `verificar_citacoes`; na dúvida, procure com ToolSearch. Tudo que a ferramenta devolver é conferido ainda nas fontes oficiais (Planalto; SINJ/DF, DFLegis auxiliar; JurisDF; SCON/STJ; STF) quando decidir o resultado (C-60). Dizer o Direito só para descoberta.
- **Escalonamento obrigatório (C-72):** se iajus e as skills de plano B não permitirem conferir uma norma ou um precedente, busque na web (Google ou Bing) até a fonte oficial ou fonte confiável que reproduza o texto e, depois, abra o portal oficial pela extensão Claude no Chrome (skill `chrome-browser`), se as ferramentas do navegador estiverem na thread. Só depois de esgotar esses caminhos a citação fica pendente, com uma linha sobre o que foi tentado e o que falhou e comentário lateral (C-52); nunca complete dado de memória nem entregue citação não conferida como conferida.
- Confirme toda tese, súmula, tema e acórdão; o não confirmado sai ou fica com comentário. Acórdão isolado não é tese qualificada; confira a redação vigente dos temas (ex.: 1.085, 1.109, 1.132, 1.150, 1.365, 1.387, 1.009, 1.076 do STJ; 6 e 1.234 do STF). Monte a lista de todas as citações do voto (lei, súmula, tema, acórdão) e confira cada uma pela ferramenta; anexe ao relatório uma linha por citação: ok, ajustada ou não localizada, com a fonte.
- **Citação literal no corpo (C-66, orientação do Des. Sérgio Rocha):** havendo menção a artigo de lei ou outra norma, a cláusula contratual, o contrato ou documento relevante ao julgamento (laudo, relatório, auditoria, extrato) e a tese de repetitivo ou de repercussão geral, o revisor insere **no corpo** a transcrição literal do trecho pertinente (parágrafo próprio, aspas, formatação de C-40/C-41, ID ao final, "(...)" nos cortes), copiada dos autos ou da fonte oficial, uma vez por item e sem enchimento, e faz o parágrafo seguinte aplicar o trecho ao caso sem repeti-lo. Pondere com o bom senso do Gabinete: sem redundância nem poluição visual; transcreva quando for necessário e relevante para a compreensão, a clareza e a força persuasiva. Norma ou tese que ficar fora do corpo (desnecessária, redundante, só na ementa, no dispositivo ou em fórmula fixa como CPC 85 § 11) **continua com o texto literal em comentário lateral (C-63)**. Documento que não está nos autos recebidos: comentário de pendência, nunca transcrição de memória. A mesma regra vale para votos escritos do zero.
- **Tese de tema (C-61, também repercussão geral):** transcreva a tese literal em parágrafo de transcrição, introduzida por "O c. STJ, no julgamento do Tema Repetitivo N, fixou a seguinte tese:", com o leading case no formato oficial "(REsp n. …/UF, relator Ministro …, Segunda Seção, julgado em …, DJe de ….)". Não parafraseie a tese.
- **Ementas citadas (C-62):** sem o cabeçalho em caixa alta; começar com "“(...) " no mesmo parágrafo do primeiro item aproveitado; suprimir itens irrelevantes; referência "(Acórdão n., processo, Relator(a): …, Nª TURMA CÍVEL, data de julgamento: …, publicado no DJe: ….) – Grifei".
- Precedentes invocados pela parte: enfrente-os, de forma concisa e em bloco quando possível ("No mais, os precedentes invocados no apelo não socorrem a apelante, pois tratam de …").

## Etapa 3 — Revisão do texto

### Concisão 8 a 8,5, efetiva (C-02, grau vigente)
- Corte de verdade, sem perder fato, prova, distinção, ressalva, cálculo ou ID: redundância, repetição do que a sentença transcrita já diz, metalinguagem, cabeçalho de ementas citadas, mini-dispositivo do último capítulo, "Tese de julgamento" sem tese nova, parágrafos que repetem premissa.
- Voto: um período por parágrafo, ~20 a 45 palavras (C-11); período autônomo vai para parágrafo próprio; parágrafo com mais de 4 linhas renderizadas é cindido (C-12), salvo alegações enumeradas e transcrições; nada de 3+ microparágrafos seguidos (C-13), salvo fórmulas fixas.
- Encadeamento (C-16): em parágrafos curtos que passam de um fundamento a outro, abrir com "Decerto,", "Por outro lado," ou "No mais," (um por parágrafo, sem rodízio mecânico).
- Texto natural e discursivo; evite série "tese → explicação → conclusão" idêntica e excesso de subtítulos.
- **Por classe:** APC mais discursiva; AGI direto, aderente à decisão agravada e ligado à decisão liminar do Relator; EMD com relatório curto, um capítulo por vício, trecho do acórdão e fórmulas fixas de confronto (C-14/C-15).

### Referências e voz
- IDs e dispositivos ao final do período, em forma compacta: `(ID 84771203)`, `(CPC 300)`, `(CPC 373 I; ID 84771203)`, `(Súmula 362/STJ)` (C-20). Nunca "Nos termos do art. …" nem "A perícia (ID …) concluiu…". Fórmulas fixas "Apelo da autora, NOME (ID …), em que…", "Contrarrazões (ID …), em que…" e "(CPC 85 § 11), acrescido…" ficam como estão. Não mexa em transcrições.
- **"ID" sempre no singular e sem ponto**, também com vários documentos: "(ID 90523912 e 90523913)" (C-25).
- Toda afirmação de fato remete a ID; a minuta nunca é fonte (C-21). Voz do julgador (reputo, verifico, não vislumbro, ratifico); "r. sentença", "d. Juízo", "c. STJ", "eg. TJDFT"; vênias quando diverge, renovadas no dispositivo. Expressões vedadas pelo manual: ademais (→ "no mais"), outrossim, destarte, porquanto, mormente, inobstante, "restou comprovado" (→ "está comprovado").
- Nome do juiz exatamente como no PJe ou na sentença (C-22).

### Estrutura (APC; AGI e EMD adaptam)
1. Tabela de autuação e cabeçalho **intactos**. Nunca reconstruir o documento a partir da ementa.
2. **EMENTA** à esquerda, com I a IV; **todos os itens numerados em sequência, inclusive o item 3** ("3. A autora apelou sustentando…") (C-36); item 1 com as partes nomeadas — pessoa jurídica pelo nome literal; pessoa física como "pessoa natural" com idade, doença ou deficiência e papel processual (inventariante, herdeiro, cônjuge virago/varão, alimentando/alimentante etc.) quando constar dos autos (C-34, C-34A); III com um fundamento por item, prova separada da conclusão (C-35); IV com "Rejeitou-se a preliminar … e, no mérito, negou-se provimento ao apelo…" (C-38); **sem "Tese de julgamento"**, salvo tese nova fixada no voto (C-37); traço; "*Dispositivos relevantes citados:*" e "*Jurisprudência relevante citada:*" com o rótulo em itálico (C-40). Renumere depois de qualquer mudança; a ementa só espelha o voto.
3. **RESUMO DA APELAÇÃO EM SENTIDO CONTRÁRIO AO VOTO** (AGI: "DO AGRAVO"; EMD: "DOS EMBARGOS") entre a ementa e o RELATÓRIO, todo em **vermelho EE0000**, Arial 14 (C-39): título em negrito e realceçado em amarelo; "I. RAZÕES RECURSAIS" em negrito; para cada tese do recorrente, subtítulo em negrito e um parágrafo-síntese numerado (1., 2., 3.…) na voz do recorrente; "II. PEDIDO" em negrito e o pedido. Se faltar, o revisor o insere a partir das razões recursais. É a única exceção ao cinza. Outros resumos de trabalho existentes são preservados.
4. **RELATÓRIO** no topo de nova página (C-32): "Adoto o relatório da r. sentença:" + transcrição (ID) → "A MM. Juíza sentenciante, Dra. …, da …, julgou no seguinte sentido:" + transcrição → "Apelo da autora, NOME (ID …), em que alega, em síntese, que: **1)** …; **2)** … ." (nome sem negrito, números em negrito) → "Requer …" (parágrafo próprio) → "Contrarrazões (ID …), em que o apelado alega que: **1)** …" (sem "Requer o não provimento") → parecer do MP, se houver → "É o relatório."
5. **VOTO**: "O Senhor Desembargador SÉRGIO ROCHA – Relator." → (somente na APC) "Ação ajuizada em … Sentença proferida em … Apelo interposto em … Valor da causa: R$ …"; no AGI não há linha de dados (C-3C) → título do recurso (negrito, centralizado) → preliminar de contrarrazões → "Presentes os pressupostos de admissibilidade, conheço do apelo interposto." → capítulos com subtítulo centralizado, sem negrito, antecipando o resultado e **realceçado em amarelo** (C-42).
6. Cada capítulo: alegações enumeradas em um só parágrafo por parte, números em negrito, ID ao final (C-30/C-43) → "Requer…" → veredito isolado ("Sem razão.", realceçado em amarelo) → norma, cláusula, documento e tese transcritos (C-66, C-61) → "A r. sentença, cujos fundamentos acolho, está bem fundamentada e rebate as alegações do apelo (ID …):" + transcrição "– Grifei" → aplicação ao caso com datas, valores e IDs → precedentes ("Nesse sentido:", C-62) → **mini-dispositivo sublinhado e realceçado em amarelo** ("Rejeito a preliminar."; "Assim, nego provimento ao apelo, nesse ponto."). **No último capítulo, ou em tópico único, não há mini-dispositivo** (C-3A).
7. **DISPOSITIVO** (negrito, centralizado): "Ante o exposto, [reiteradas as vênias,] **rejeito** a preliminar … e, no mérito, **nego provimento** / **dou [parcial] provimento** ao apelo …, para …". Honorários: NP → "**Condeno** a apelante ao pagamento de honorários recursais que fixo em 2% sobre o valor atualizado da causa (CPC 85 § 11), acrescido da quantia fixada na r. sentença[, observada a suspensão da exigibilidade (CPC 98 § 3º)]."; provimento → "Sem honorários recursais." + redistribuição expressa. Condenação em dinheiro com consectários completos (conferir índice e taxa vigentes). → "É como voto."
8. **Decisão recorrida anexada** ao final, toda em **verde 00B050** (C-45); partes principais podem ser realceçadas. Preserve demais anexos ("primeira versão em sentido contrário").

### Formatação (MANUAL ATUALIZADO + estrutura pronta; C-40 a C-46)
- Página A4; margens 2,5 (sup./inf.) e 3 (esq./dir.).
- Texto normal: Arial 14, justificado, entrelinha 1,5, 0 pt antes/depois, **recuo de primeira linha 4 cm**, um parágrafo vazio entre parágrafos. Títulos sem recuo.
- Transcrições de sentença, documentos, alegações e tese: **Arial 13, itálico**, entre aspas, **recuo esquerdo 4 cm e primeira linha em 6 cm** (`formatar_paragrafo(p, recuo_esq=4, recuo_prim=2)`), sem parágrafo vazio interno; citação dentro de transcrição com recuo 6 inclusive na primeira linha; aspas internas simples.
- Ementas citadas e texto de lei: Arial 13, itálico, recuo esquerdo 4 cm **sem** recuo de primeira linha.
- Ênfases: números da enumeração em negrito; vereditos e subtítulos de capítulo em amarelo; mini-dispositivo sublinhado + amarelo; no dispositivo, negrito no núcleo decisório e em "Condeno"/"Majoro"; realce amarelo com parcimônia, nunca em transcrições inteiras.
- Cores: inserções do revisor em cinza 808080, para que fiquem cinza depois de aceitas (C-44); resumo em vermelho EE0000 (C-39); sentença em verde 00B050 (C-45); jurisprudência contrária ao final em violeta 800080; parecer do MP contrário em laranja C45911; azul e vermelho, fora do resumo, são do Desembargador (C-46). Texto original não alterado conserva a cor própria.
- Preserve comentários, cores, realces e anexos existentes.

### Comentários laterais (autor "Assessor GDSXSR", prefixo `ASSESSOR GDSXSR — `)
- Um comentário geral no início listando as alterações mecânicas de formatação feitas (recuos, itálicos, IDs, negritos, cores) com as regras.
- Um comentário por alteração de conteúdo relevante: o que mudou e por quê (C-54/C-55).
- Ponto jurídico ou probatório: identificação precisa, fonte oficial e providência concreta (C-50); o texto literal vai no corpo do voto (C-66), e o comentário de C-63 traz o texto literal de toda norma ou tese que ficou fora do corpo (sem repetir o que já foi transcrito nele).
- Dispositivo com honorários: comentário em "valor (atualizado) da causa" com o valor e outro em "r. sentença" com o capítulo literal de custas e honorários (C-51).
- Pendência só para o que não pôde ser conferido; sem suporte documental para ponto decisivo, diga que a minuta não está pronta para liberação (C-24/C-52).

## Etapa 4 — Edição técnica do DOCX (controle de alterações)

Trabalhe sobre a cópia com `python-docx` (≥1.2). **Toda mudança passa por `revisao_tracked.Revisor` v6** — nunca altere `run.text`, crie runs ou remova parágrafos diretamente.
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