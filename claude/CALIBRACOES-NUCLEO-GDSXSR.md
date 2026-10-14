# CALIBRAÇÕES — NÚCLEO (todas as classes) — ASSESSOR GDSXSR

**Versão:** v18 · **Data-base:** 14/10/2026 · divisão do arquivo único v16 em núcleo + classe + registro (aprovada por Marcos em 13/10/2026; nenhuma regra foi apagada).
**Onde está o quê:** este arquivo traz as regras que valem para APC, AGI e EMD. Regras de uma só classe estão em `CALIBRACOES-APC-GDSXSR.md`, `CALIBRACOES-AGI-GDSXSR.md` e `CALIBRACOES-EMD-GDSXSR.md` (ler só a da classe da minuta). Registro de alterações por versão: `historico/REGISTRO-ALTERACOES-CALIBRACOES.md`. Texto integral anterior, com todas as "Origem:" (processo, data, quem corrigiu): `historico/CALIBRACOES-VIGENTES-GDSXSR-v16-completo.md` (consultar só para auditoria).
**Novas calibrações** entram pela skill `registrar-calibracao`: regra geral aqui; regra de uma classe no arquivo da classe; "Origem" e linha da versão no registro.
**Hierarquia em conflito:** instrução do usuário para a minuta atual → regra mais recente e específica → MANUAL ATUALIZADO e estruturas prontas do Drive (formatação) → perfis de estilo (APC, PASEP, AGI, EMD; o `PERFIL-ESTILO-GDSXSR-v1.1.md` é histórico) → modelos do Drive.
**Status:** ATIVA · SUBSTITUÍDA (só no histórico) · ESPECÍFICA (só para a matéria indicada).

---

## A. Princípios

**C-01 · Objetivo de estilo** — ATIVA · todas · v1.1
O voto não deve parecer escrito por IA. Prioridade: clareza → fidelidade → naturalidade → fluidez → concisão moderada. Pergunta final: "parece escrito ou aperfeiçoado por alguém do Gabinete?".

**C-02 · Concisão 8 a 8,5, efetiva** — ATIVA · todas · v1.1, v2, v3, v6, v8
**Grau vigente: 8 a 8,5 (confirmado por Marcos em 13/10/2026). A referência "7/10" de v1.1–v6 está superada.** Eliminar redundância, repetição de premissa ou conclusão, metalinguagem, duplicação de alegações e transcrição dispensável. Sem meta percentual de redução. Não omitir argumento capaz de alterar o resultado, ressalva probatória, distinção de precedente, cálculo, identificação documental ou limite do dispositivo. **v6:** a concisão tem de aparecer no resultado — o revisor corta, não apenas reorganiza. Cortes típicos: cabeçalho (verbetação) das ementas transcritas (C-62); mini-dispositivo do último capítulo (C-3A); "Tese de julgamento" sem tese nova (C-37); parágrafo próprio que só repete o que a sentença transcrita já diz; enfrentamento de precedentes em bloco ("No mais, os precedentes invocados no apelo não socorrem a apelante, pois tratam de débito superior ao pactuado e de empréstimos não solicitados…"), sem um parágrafo por acórdão. Técnica preferida: fundir parágrafos consecutivos de uma só ideia que repetem ou completam a mesma premissa (ex.: "Os documentos técnicos também confirmam…" + "A existência do prejuízo, portanto, não é o ponto central…" → um só período), suprimir o parágrafo que antecipa a conclusão do capítulo e qualificações acessórias ("veiculada nas contrarrazões", "como defesa indireta"). Meta indicativa no voto: −10% a −20% de palavras em relação à primeira revisão, sem regredir à fragmentação (C-13).

**C-03 · Fidelidade** — ATIVA · todas · v1.0, v2, v3
Não alterar fatos, pedidos, provas, valores, datas, fundamentos essenciais ou resultado por estilo. Não presumir prova ausente nem transformar narrativa de peça em fato incontroverso. Revisar ementa, relatório, voto e dispositivo em conjunto.

**C-04 · Preservação do original** — ATIVA · todas · v1.0, v3
Trabalhar sobre cópia; registrar hash. Preservar integralmente cabeçalho, logotipo, tabela de autuação, margens, cores, comentários anteriores, realces, resumos de trabalho e peças anexadas. Nunca reconstruir o documento a partir da ementa.

**C-05 · Autoridade de estilo × autoridade jurídica** — ATIVA · todas · v1.1, v3, v6
Modelos do Drive definem forma, estrutura, cadência e prática; fontes oficiais atuais definem lei e jurisprudência vigentes. O modelo não prova fatos do processo revisado. Consultar 3 a 8 modelos (OURO → corrigidos/alterados/liberados pelo Desembargador → "Marcos" → mesma classe e resultado → mesma matéria → corpus geral). Minuta não aprovada não vira MODELO OURO. **v6:** a formatação segue obrigatoriamente o MANUAL ATUALIZADO e a estrutura pronta da classe (pasta de estruturas do Drive, id 1aEgy58IgkjNOvu0zAYhREeOXViIZeUHI): ler as duas antes de revisar.

## B. Parágrafo e cadência

**C-11 · Um período por parágrafo no voto** — ATIVA · todas, sobretudo APC · v4
No voto, o padrão é um período por parágrafo, de cerca de 20 a 45 palavras. Se o parágrafo tem premissa ou regra seguida de período autônomo (conclusão, aplicação, reforço), o segundo ganha parágrafo próprio. Dois períodos juntos só quando o segundo não se sustenta sozinho. Confirmado pelas versões corrigidas de 2026 (perfil APC).

**C-12 · Limite de 4 linhas renderizadas** — ATIVA · todas · v2, v3
Parágrafo editorial com mais de 4 linhas no DOCX renderizado é cindido no ponto lógico, por quebra real de parágrafo, sem dividir oração. Contagem de palavras serve só para triagem. Exceções: parágrafo único de alegações enumeradas; transcrições.

**C-13 · Vedação de fragmentação** — ATIVA · todas · v1.1, v4
Três ou mais parágrafos livres seguidos com menos de 15 palavras exigem revisão. Exceções: títulos, "Com razão./Sem razão./Com parcial razão.", admissibilidade, "É o relatório.", "É como voto.", mini-dispositivo, dispositivo e transcrições.

**C-14 · Cadência e arquitetura por classe** — ATIVA · v1.1, v5
**Linha de dados do voto ("Ação ajuizada em… Valor da causa"): permanece na APC; não existe no AGI (C-3C, arquivo AGI).** APC: mais discursiva, articula fato, prova, norma, precedente e consequência (perfil APC). AGI: direto, aderente à decisão agravada e ligado expressamente à decisão liminar do Relator — manter as razões, reconhecer a probabilidade já vista ou refluir em cognição exauriente (`claude/PERFIL-AGI-GDSXSR-2026-10-06.md`). EMD: relatório curto (ementa do acórdão + uma linha sobre os vícios), um capítulo por vício, com o trecho do acórdão que enfrentou a questão; prequestionamento e efeitos infringentes só se suscitados (`claude/PERFIL-EMD-GDSXSR-2026-10-06.md`).

**C-15 · Sinais de texto artificial a eliminar** — ATIVA · todas · v1.1
Série de parágrafos de uma linha; mesma construção sintática repetida; frases conclusivas soltas ("Assim.", "Logo."); reapresentação de fundamento já demonstrado; conectores decorativos; esquema "tese → explicação → conclusão" idêntico em todos os capítulos; excesso de títulos. **Exceção (v5):** nos EMD, as fórmulas fixas de confronto do Gabinete ("A alegação de omissão não merece prosperar…", "O v. acórdão embargado, portanto, cumpriu sua finalidade…", "Na verdade, ao alegar…") são padrão da casa e devem ser mantidas, desde que acompanhadas do trecho do acórdão que as sustenta.

**C-16 · Encadeamento entre parágrafos de um período** — ATIVA · todas · v6
Quando parágrafos curtos consecutivos passam de um fundamento a outro (abuso de direito → impenhorabilidade → informação → mínimo existencial → precedentes), abrir o parágrafo com conector que marque a passagem: "Decerto," (reforço da premissa), "Por outro lado," (fundamento distinto), "No mais," (último ponto, C-23). Um conector por parágrafo, sem rodízio mecânico. Exemplo: "A impenhorabilidade dos proventos protege…" → "Por outro lado, a impenhorabilidade dos proventos protege…".

## C. Referências e voz

**C-20 · ID e dispositivo legal ao final do período** — ATIVA · todas · v1.1
Forma compacta entre parênteses: (ID 84771203), (CPC 300), (CPC 373 I; ID 84771203). Evitar "Nos termos do art. …" e "A perícia (ID …) concluiu…". Transcrições literais ficam intactas. Fórmulas fixas do relatório ("Apelo da autora, NOME (ID …), em que alega…"; "Contrarrazões (ID …), em que…") e do dispositivo ("(CPC 85 § 11), acrescido…") não são deslocadas. **v15:** a forma compacta vale também na ementa: "(CPC 1.022)", "(CPC 489 § 1º IV)", "(CC 884)", "(LINDB 20)", "(CDC 42 parágrafo único)", sem "art." e sem vírgula depois da sigla (EMD 0707899-35; Marcos, 11/10/2026). **v15 (observada):** quando o ID é de peça dos autos de origem (e não do agravo), o ID leva a indicação: "(ID 284303352, do processo de origem)".

**C-21 · A minuta nunca é fonte** — ATIVA · todas · v3
Toda afirmação de fato ou prova remete a ato, documento ou ID dos autos. Vedado "a minuta aponta", "a revisão demonstrou" e fórmulas semelhantes na voz do julgador.

**C-22 · Nome do juiz sentenciante** — ATIVA · todas · v4
Usar a forma exata confirmada no PJe, sem completar nem acrescentar partículas (ex.: "Itamar Dias Noronha", não "… Filho"). Se a sentença não identificar o juiz, comentário de conferência.

**C-23 · "No mais" em vez de "ademais"** — ATIVA · todas · v4, v8, v14, v15
Para acrescentar um último elemento. **v8 (observada):** preferir o pretérito perfeito ao mais-que-perfeito sintético na narrativa do voto ("a prescrição já foi arguida", não "já fora arguida"). O manual também veda "ademais", "outrossim", "destarte", "porquanto", "mormente", "inobstante", "restou comprovado" (usar "está comprovado"). **v15:** "No caso," abre o parágrafo que aplica a premissa ao caso concreto ("No caso, essas questões já foram…", não "Essas questões já foram…"; também no lugar de "Na espécie", como em v11).

**C-24 · Sem inteiro teor** — ATIVA · todas · v3
Conferir apenas o que o material recebido reproduz; declarar a limitação em comentário e no relatório de entrega. Ponto decisivo sem suporte documental impede considerar a minuta pronta para liberação.

**C-25 · "ID" sempre no singular e sem ponto** — ATIVA · todas · v6
Também com vários documentos: "(ID 90523912 e 90523913)", nunca "(IDs …)" nem "ID." (manual, 2.3.3).

**C-26 · Mudança de entendimento do Relator fica no comentário** — ATIVA · todas · v9
O voto não narra que o Relator refluiu de entendimento adotado em outros processos ("Reexaminada a controvérsia, refluo do entendimento adotado por este Relator em casos anteriores…"); o parágrafo é suprimido e o voto segue a liminar e os fundamentos do caso. A divergência com a linha anterior fica só no comentário lateral (C-53). Não vale para o refluxo em relação à própria liminar do processo (perfil AGI, "Reexaminando a controvérsia em cognição exauriente…").

**C-27 · Vocabulário: "cumprimento de sentença" não é ação; "cônjuge" é masculino; sem "por ora"** — ATIVA · todas · v15
(a) Cumprimento de sentença é fase, não ação: "Cumprimento de sentença proposto por B6 Assignee…" (não "Ação de cumprimento de sentença proposta…", AGI 0734154-26). (b) "cônjuge" é substantivo masculino: "bens do cônjuge", "o cônjuge" (não "da cônjuge", "a cônjuge"); para indicar que se trata da mulher, "o cônjuge virago" (AGI 0732074-89, ementa itens 2 e 9). (c) Ao resumir a decisão agravada, suprimir o hedge "por ora" ("que indeferiu o bloqueio", não "que indeferiu, por ora, o bloqueio"; AGI 0732074-89). (d) **v16 (observada, EMD 0705293-30):** ao apontar o erro do julgado embargado, falar em "dispositivo do acórdão", e não em "dispositivo do voto condutor" (Marcos trocou na frase do erro material; manteve "voto condutor" no dispositivo, então caso único). Motivo inferido (precisão técnica; o "por ora" sugere provisoriedade que a decisão não declarou), não declarado por Marcos.

## D. Estrutura

**C-30 · Alegações enumeradas em parágrafo único** — ATIVA · todas · v2, v4
No relatório e no voto, as alegações de cada parte e manifestação ficam em um só parágrafo, com 1), 2), 3)…, mesmo acima de quatro linhas, com o ID ao final. Acrescentar a enumeração quando faltar, sem omitir nem inventar fundamentos. Não se aplica a transcrições. Os números vão em negrito (C-43).

**C-31 · Relatório sem "Requer o não provimento do recurso."** — ATIVA · todas · v4
A fórmula é suprimida após as contrarrazões. O "Requer …" do recorrente continua em parágrafo próprio.

**C-32 · RELATÓRIO no topo da página** — ATIVA · todas · v4, v6
O título começa no topo da página seguinte ao fim do bloco anterior (ementa ou resumo, C-39), sem parágrafos vazios excedentes. Conferir no PDF.

**C-33 · Ementa espelha o voto** — ATIVA · todas · v3
Não introduzir na ementa prova, tese ou resultado ausente do voto. Classificação, número de recursos e comando final devem coincidir.

**C-34 · Ementa, item 1: "pessoa natural"** — ATIVA · todas · v4, v8, v14
Qualificar a parte autora pessoa física como "pessoa natural" ("Ação proposta por consumidor pessoa natural contra …"). **v8:** quando a ação tem nome próprio, o item 1 começa por ele, sem "Ação de": "1. Embargos de terceiro propostos por pessoas naturais contra o Distrito Federal…" (não "Ação de embargos de terceiro proposta…").

**C-35 · Ementa, "III. Razões de decidir": um fundamento por item** — ATIVA · todas · v4, v15
Prova em um item, consequência jurídica em outro. Renumerar todos os itens depois, inclusive "IV. Dispositivo". Mantida na versão final de 06/10/2026 (itens 8/9 e 11/12 desmembrados pelo revisor foram aceitos). **v15 (refinamento):** o item que reúne a premissa geral e a aplicação ao caso é cindido em dois — na EMD 0716247-18, o item 5 (64 palavras, 3 períodos: "Inexiste omissão quando o acórdão aprecia…" + "As matérias apontadas… (CPC, art. 505, I)") virou os itens 5 e 6, e o dispositivo passou de 8 para 9. O mesmo vale para o item 6 da EMD 0707006-20 (omissão × contradição em itens separados), cuja numeração seguinte foi deslocada. Na AGI 0743704-45 o item 6 (62 palavras: inexistência de título executivo + "as demais insurgências… excesso de execução") virou dois itens e o dispositivo passou de 11 para 12.

**C-36 · Ementa numerada em sequência, inclusive o item 3** — ATIVA · todas · v6
**Mantida por Marcos em 13/10/2026: o item 3 permanece numerado; perfis antigos que dizem "sem enumeração" estão superados.** Todos os itens de I a IV levam número seguido de ponto (1., 2., 3., 4. …), também o item 3 de "I. Caso em exame" (razões do recurso). Substitui a orientação anterior da skill e do perfil APC ("item 3 sem enumeração"). Exemplo: "A autora apelou sustentando…" → "3. A autora apelou sustentando…".

**C-37 · Sem "Tese de julgamento" na ementa** — ATIVA · APC (e demais classes, salvo tese nova) · v6
A estrutura pronta não prevê "Tese de julgamento". Suprimi-la quando o voto apenas aplica tese já firmada (tema repetitivo, súmula) ou mantém a sentença; manter só se o voto fixar entendimento novo, e então com comentário.

**C-38 · Fórmula preliminar + mérito** — ATIVA · todas · v6, v15
Havendo preliminar, ementa e dispositivo usam "e, no mérito,": "14. Rejeitou-se a preliminar de não conhecimento e, no mérito, negou-se provimento ao apelo da autora." / "Ante o exposto, **rejeito** a preliminar … e, no mérito, **nego provimento** ao apelo…". Não se conheceu da alegação de prescrição deduzida em contrarrazões e, no mérito, negou-se provimento…" / "Ante o exposto, não conheço da alegação de prescrição, veiculada nas contrarrazões, e, no mérito, nego provimento…". Conferir ementa, voto e dispositivo juntos antes da entrega.

**C-39 · Resumo do recurso em sentido contrário ao voto** — ATIVA · APC, AGI, EMD · v6
Entre a ementa ("Jurisprudência relevante citada") e o RELATÓRIO vai o bloco de trabalho do resumo (na estrutura pronta, "RESUMO COPILOT"), em **vermelho EE0000**, Arial 14:
- título "RESUMO DA APELAÇÃO EM SENTIDO CONTRÁRIO AO VOTO" (no AGI, "DO AGRAVO"; nos EMD, "DOS EMBARGOS"), em negrito e realçado em amarelo;
- "I. RAZÕES RECURSAIS" em negrito; para cada tese do recorrente, subtítulo em negrito e um parágrafo-síntese numerado (lista automática 1., 2., 3.…), na voz do recorrente ("A apelante sustenta…", "Alega…", "Afirma…");
- "II. PEDIDO" em negrito e o pedido em um parágrafo.
Serve para o Desembargador ver o melhor argumento contrário. Se a minuta não o tiver, o revisor o insere (rastreado), com base nas razões recursais dos autos. É a única exceção ao cinza de C-44 e à reserva do vermelho (C-46). Observada e mantida por Marcos na AGI 0732049-76, 08/10/2026 (caso único; reconfirmar se reaparecer).

**C-3A · Mini-dispositivo de capítulo** — ATIVA · todas · v6
Cada capítulo, exceto o último, termina com a conclusão sublinhada e realçada em amarelo ("Rejeito a preliminar." / "Assim, nego provimento ao apelo, nesse ponto." / "Dou provimento ao apelo, nesse ponto, para…"). No último capítulo, ou em tópico único, não há mini-dispositivo: o voto segue direto para o DISPOSITIVO. Exemplo: "Nego provimento ao apelo, nesse ponto." antes do DISPOSITIVO → suprimir. **v18 (observada, APC 0711608-24):** o veredito de provimento parcial é "Com parcial razão." (não "Em parte com razão."); o mini-dispositivo abre com "Assim, dou parcial provimento ao apelo para …" e traz a consequência (valor, parte excluída), sem repetir o que o capítulo já disse. **v16 (observada, EMD):** quando o capítulo acolhe os embargos, o mini-dispositivo indica a finalidade do acolhimento: "Assim, dou provimento aos embargos de declaração, nesse ponto, sem efeitos infringentes, para sanar a obscuridade e erro material existentes." (EMD 0705293-30, Marcos, 13/10/2026; caso único, em tensão com a brevidade de v8, que continua valendo para o não acolhimento). **v15:** vírgula antes de "nesse ponto" também no AGI: "Assim, nego provimento ao agravo de instrumento, nesse ponto." (AGI 0731896-43, Marcos, 11/10/2026).

**C-3F · Dispositivo em parágrafo único** — ATIVA · todas · v15
O DISPOSITIVO é um único parágrafo; a determinação consequente entra na mesma frase por "a fim de que", e não em segundo parágrafo iniciado por "Determino". Exemplo (AGI 0731334-34): "…dou provimento ao agravo de instrumento das exequentes, … para confirmar a liminar**, a fim de que** o novo edital de leilão, com as retificações já definidas na origem, seja expedido independentemente da preclusão das decisões de ID …" (eram dois parágrafos; "Determino" foi rejeitado). Caso único até aqui; motivo inferido do padrão da estrutura pronta (dispositivo contínuo), não declarado.

## E. Formatação

**C-40 · Fontes** — ATIVA · todas · v3, v6
Arial 14 no texto editorial (ementa, relatório, voto, títulos, dispositivo). Transcrições (sentença, documentos, alegações, ementas, lei, tese) em **Arial 13 e itálico**, entre aspas; aspas internas viram simples. Na ementa, os rótulos "Dispositivos relevantes citados:" e "Jurisprudência relevante citada:" em itálico (só o rótulo). Não aplicar Arial 13 nem itálico aos anexos.

**C-41 · Página, espaçamento e recuos** — ATIVA · todas · v2, v6
- Página A4; margens superior e inferior 2,5 cm, esquerda e direita 3 cm.
- Texto normal: justificado, entrelinha 1,5, espaçamento 0 pt antes e depois, **recuo de primeira linha 4 cm** (não 2,54), um parágrafo vazio entre parágrafos normais.
- Transcrição de sentença, documento ou alegação: **recuo esquerdo 4 cm e primeira linha em 6 cm** (recuo especial de 2 cm), sem parágrafo vazio interno. Citação dentro de transcrição: recuo 6 cm, inclusive a primeira linha.
- Ementa transcrita e texto de lei: recuo esquerdo 4 cm, **sem** recuo de primeira linha. Tese de tema transcrita: como trecho (4 cm / 6 cm), conforme a versão final.
- Títulos e subtítulos sem recuo de primeira linha; "O Senhor Desembargador SÉRGIO ROCHA – Relator." sem recuo.


**C-42 · Títulos** — ATIVA · todas · v2, v3, v6, v15
Títulos e subtítulos da ementa sempre à esquerda (EMENTA, I a IV). Entre RELATÓRIO e DISPOSITIVO, títulos e subtítulos de fundamentação centralizados. Título do recurso em negrito; subtítulo de capítulo sem negrito, antecipando o resultado ("DA REJEIÇÃO DA PRELIMINAR DE…") e **realçado em amarelo**; DISPOSITIVO em negrito. O veredito isolado ("Sem razão.", "Com razão.") também vai realçado em amarelo.

**C-43 · Ênfases** — ATIVA · todas · v2, v4, v6, v15
- Relatório e voto: os números da enumeração das alegações — 1), 2), 3)… — em **negrito** (manual 2.3.5); o nome da parte no "Apelo da autora, NOME (ID …)" **sem** negrito.
- Mini-dispositivo de capítulo sublinhado e em amarelo (C-3A).
- Dispositivo: negrito no núcleo decisório (**rejeito**, **nego provimento**, **dou parcial provimento**) e no verbo de honorários (**Condeno**, **Majoro**).
- Realce amarelo com parcimônia nos pontos centrais da fundamentação, nunca em transcrições inteiras. A cor das alterações do revisor segue C-44.
- **v8 — pontos mais importantes do voto em amarelo:** além de subtítulos, vereditos e mini-dispositivos, realçar em cada capítulo os 2 a 4 períodos que decidem a questão — a premissa jurídica decisiva, o fato provado (ou não provado) que a resolve e a conclusão. Ex.: "Essa possibilidade não equivale à prova do nexo causal…"; "A expressão 'limitado a um desconto de' institui teto de retenção, e não piso…". Não realçar alegações, relatório, transcrições inteiras nem parágrafos de passagem.
- **v15 (reforço):** na EMD 0707899-35 Marcos acrescentou realce amarelo a cinco períodos decisivos do voto (o fundamento do acórdão, o ponto não enfrentado, o PIX de R$ 7.485,67 com ID, a devolução do valor); o agente havia realçado pouco em EMD. Dois parágrafos curtos seguidos que se completam foram fundidos em um ("A conta de destino é a indicada no contrato… (ID …). É a mesma em que o autor recebe o benefício… (ID …).", C-11/C-13).


**C-44 · Controle de alterações com texto em cinza** — ATIVA · todas · v5, v6
Toda alteração do revisor é entregue como alteração rastreada do Word (autor "Assessor GDSXSR"): inserções em w:ins, exclusões em w:del, cisões com a marca de parágrafo inserida, recuos e alinhamento em w:pPrChange, negrito/itálico/tamanho/realce/sublinhado em w:rPrChange. O texto inserido já vai na cor 808080, de modo que, **aceita a alteração, o texto permanece cinza**; o texto excluído some ao aceitar. Texto original não alterado conserva a cor própria. **v6:** parágrafo com comentário **também é reescrito** — as âncoras do comentário são preservadas pela ferramenta; só parágrafo com campo, hiperlink, nota ou imagem fica protegido. Única exceção de cor: o resumo em vermelho (C-39). Confirmação: Marcos manteve em cinza as inserções do revisor e escreveu as próprias também em cinza (06/10/2026). **v7 — SUBSTITUÍDA quanto à forma de entrega por C-47:** o controle de alterações passa a ser só instrumento interno de trabalho (portão e conferência); o arquivo entregue sai com as alterações já aplicadas.

**C-47 · Entrega com alterações já aplicadas, em cinza, só com comentários** — ATIVA · todas · v7
**Confirmada por Marcos em 13/10/2026: a entrega é o DOCX com as alterações do revisor já aceitas; o rastreado fica só em `entregas/rastreados/`.** O assessor não aceita nem rejeita alteração por alteração. O revisor edita com `revisao_tracked.Revisor` (para o portão `checar_voto.py` conferir), mas **entrega o DOCX com todas as alterações do autor "Assessor GDSXSR" já aceitas** (`aceitar_autor.py`, que aceita só as marcas do revisor): o texto novo fica em cinza 808080 (resumo em vermelho, C-39), o texto excluído desaparece, e cada alteração relevante fica explicada em comentário lateral (C-54/C-55). Alterações rastreadas de terceiros já existentes na minuta (ex.: de outro assessor) são preservadas como estão, e o portão acusa inserção "sem cinza" apenas por elas — justificar no relatório.

**C-45 · Decisão recorrida anexada em verde** — ATIVA · todas · v6
A sentença (ou decisão agravada, ou acórdão embargado) vai ao final do documento, depois de "É como voto.", inteira na cor **verde 00B050**; as partes principais podem ser realçadas (manual: "realçando em marrom as partes principais").

**C-46 · Cores reservadas e blocos finais** — ATIVA · todas · v6
Azul e vermelho são do Desembargador (azul: o que vai ler na sessão; vermelho: o que discorda); o revisor não os usa, salvo o resumo de C-39. Jurisprudência em sentido contrário ao voto vai **ao final, em violeta 800080**, sinalizada em comentário no início do documento; parecer da Procuradoria em sentido contrário, ao final, em laranja C45911.

## F. Comentários laterais

**C-50 · Comentário jurídico com texto literal** — ATIVA · todas · v2, v3
Em ementa, relatório e voto, quando houver ponto jurídico ou probatório: trecho literal da lei ou tese, identificação precisa, fonte oficial e providência concreta (ID a conferir, efeito de resultado contrário). Referência solta ("CPC 371", "Tema 972") é insuficiente. Distinguir literal de paráfrase. Preservar comentários anteriores.

**C-51 · Comentários de honorários no dispositivo** — ATIVA · todas · v4
Ao fixar ou majorar honorários recursais: comentário em "valor (atualizado) da causa" com o valor; comentário em "r. sentença" com a transcrição literal do capítulo de custas e honorários (percentual, base, dispositivos, suspensão por gratuidade).

**C-52 · Comentários de pendência** — ATIVA · todas · v4, v6
Pendência só para o que **não** pode ser conferido com o material disponível (fato fora dos autos recebidos, documento ilegível). O que o revisor pode conferir, ele confere e corrige. São instrumento de trabalho: o assessor os apaga ao resolver; os de conteúdo normativo literal permanecem na versão final.

**C-53 · Divergência com a linha decisória** — ATIVA · todas · perfis decisórios de 05/10/2026, v6
O revisor não altera o **resultado** do julgamento (C-03). Divergência da linha do Gabinete vai para comentário, com o modelo de referência e o fato que a justificaria. **v6:** jurisprudência contrária relevante (inclusive a invocada pela parte) não fica como pergunta: o revisor a enfrenta no texto quando for distinguível ou a coloca ao final, em violeta (C-46), com comentário que diz o que fez.

**C-54 · O revisor altera, não sugere** — ATIVA · todas · v6
Toda melhoria que o revisor identificar é **feita no texto** (em cinza, rastreada, C-44) — inclusive em parágrafos com comentário, fórmulas, linha de dados, ementa e dispositivo —, e cada alteração relevante recebe comentário lateral curto que explica **o que foi alterado e por quê**, com a regra aplicada: "ASSESSOR GDSXSR — Alterei 'Recurso interposto' para 'Apelo interposto' e incluí os dois-pontos em 'Valor da causa:', conforme a estrutura pronta APC (C-54)." Proibido deixar a decisão ao assessor ("Sugestão…", "Sugiro…", "Decidir se…", "Avaliar se…", "a critério"). Limites: não mudar o resultado (C-03/C-53) nem fato sem prova nos autos (C-24).

**C-55 · Comentário diz o que foi feito** — ATIVA · todas · v6
Os comentários são a comunicação com o Desembargador: concisos, pertinentes, sobre o que foi alterado e os pontos sensíveis (manual 2.3.9: "As alterações e correções devem ser inseridas em texto colorido. Mencione no comentário lateral o que foi feito"). Alterações de mesma natureza (recuos, itálicos, IDs) recebem um único comentário geral no início do documento, não um por parágrafo.

## G. Jurisprudência e legislação

**C-60 · Confirmação em fonte oficial** — ATIVA · todas · v1.1, v2, v3
Legislação: Planalto; SINJ/DF (DFLegis auxiliar). Jurisprudência: JurisDF, SCON/STJ, STF; Dizer o Direito só para descoberta. Acórdão isolado não é tese qualificada. Citação não confirmada é retirada ou sinalizada em comentário. Modelo antigo não torna vigente o que cita. **v16 (observada):** o registro de precedentes do iajus pode estar defasado em relação à fonte oficial. Na EMD 0705293-30 o iajus (12/10/2026) marcava o Tema 1.230/STJ como pendente de julgamento, a minuta escreveu que não havia tese e Marcos informou que o tema já fora julgado (REsp 1.894.973/PR, Corte Especial, sessão virtual de 8 a 15/9/2026, DJEN de 21/9/2026). Quando o iajus disser "pendente" ou "sem tese", o revisor não afirma isso no voto sem conferir o andamento no site do STJ, ou declara em comentário que não conseguiu conferir; o inteiro teor enviado pelo usuário prevalece sobre o registro.

**C-61 · Tese de tema transcrita literalmente** — ATIVA · todas · v6
Quando o voto se apoia em tema repetitivo ou de repercussão geral, a tese é transcrita literalmente, em parágrafo de transcrição (C-40/C-41), introduzida por "O c. STJ, no julgamento do Tema Repetitivo 1.085, fixou a seguinte tese:" e seguida do leading case no formato oficial: "(REsp n. 1.863.973/SP, relator Ministro Marco Aurélio Bellizze, Segunda Seção, julgado em 9/3/2022, DJe de 15/3/2022.)". Não parafrasear a tese no corpo. A tese é aplicada requisito a requisito ao caso em parágrafos curtos ("Quanto ao requisito (a)…"; "No mais, quanto ao requisito (b)…"), e a ementa do voto cita o tema na rubrica da jurisprudência ("REsp nº 1.894.973/PR (Tema 1.230)"). Não confirmado por Marcos além da manutenção da estrutura; observada.

**C-62 · Ementa de precedente transcrita sem cabeçalho** — ATIVA · todas · v6
Na citação de jurisprudência, suprimir o cabeçalho (verbetação em caixa alta) e os itens irrelevantes; a transcrição começa com "“(...) " no mesmo parágrafo do primeiro item aproveitado ("“(...) 2. Nos termos do Tema 1.085 do STJ…"), sublinhando o mais importante, e termina com a origem: "(Acórdão n., processo, Relator(a): NOME, Nª TURMA CÍVEL, data de julgamento: …, publicado no DJe: ….) – Grifei". Exceção: no relatório dos EMD, a ementa do acórdão embargado vai completa. (...)”") e ponto final depois de "(...)" quando o corte interrompe a frase ("pela escrituração contábil (...).”"), sempre dentro das aspas (AGI 0740323-29, 0738060-24).

**C-63 · Comentário com o texto literal de dispositivo, súmula ou tese** — ATIVA · todas · v8
Sempre que o voto (ou a ementa, o relatório e o dispositivo, quando a menção só aparece ali) mencionar dispositivo de lei, súmula ou tese vinculante do STJ ou do STF (repetitivo, repercussão geral, súmula vinculante), o revisor cria comentário lateral que o transcreve **entre aspas**, com a identificação precisa e a fonte oficial: "ASSESSOR GDSXSR — Texto literal (C-63): CPC, art. 373, I: “Art. 373. O ônus da prova incumbe: I - ao autor, quanto ao fato constitutivo de seu direito;” (fonte: Planalto)". Um comentário por dispositivo, ancorado na primeira menção no voto; vários dispositivos do mesmo período ficam no mesmo comentário. Transcrever só o caput e o inciso ou parágrafo citado (com "(...)" para o que se omite), sem as anotações do Planalto ("Redação dada…", "Incluído…"). Não se aplica a dispositivos citados dentro de transcrições da sentença ou de precedentes.

**C-64 · Conferir a vigência do dispositivo citado** — ATIVA · todas · v8
Ao transcrever o dispositivo (C-63), conferir no Planalto se ele foi revogado ou alterado. Se o fato for anterior à revogação, manter a norma da época e dizê-lo no texto e na ementa, indicando a norma atual: "(CC 786, vigente à época; Lei 15.040/2024 94)"; se posterior, substituir pela norma vigente. Comentar a mudança com as datas.

**C-65 · Um precedente por tese; ementa só lista o que o voto usa** — ATIVA · AGI (e demais, quando houver mais de um precedente para a mesma tese) · v9
Cada tese recebe um precedente transcrito; cortar o segundo ("No mesmo sentido:" + ementa + "– Grifei") e o parágrafo de "caso semelhante" que só introduz outro acórdão. "Jurisprudência relevante citada" na ementa lista apenas os precedentes que continuam no voto. **v16 (observada, EMD):** precedente que o acórdão embargado já citou não é reapresentado com número no voto dos embargos, salvo se for o ponto discutido. Na EMD 0705293-30 Marcos suprimiu "e no entendimento da Corte Especial do STJ (EREsp 1.582.475/MG)" da frase "O arresto se funda nos CPC 300 e 301…"; o ônus segue só com a lei. **v18 (observada, APC 0711608-24):** não se transcreve acórdão (nem se lista na ementa) que só responde a ponto não impugnado no apelo; Marcos cortou o precedente do próprio Relator sobre a legitimidade do banco, porque o apelo não a discutia.

**C-66 · Lei decisiva transcrita no corpo do voto** — ATIVA (observada) · APC · v18
Quando o capítulo depende do texto da lei, o voto o transcreve em bloco, um dispositivo por transcrição (caput com incisos em parágrafos separados), introduzido por frase curta que termina em dois-pontos ("Por outro lado, o CDC 7º parágrafo único e 25 § 1º, e o CC 265 dispõem:"). Vale como complemento do comentário literal (C-63), que continua. Marcos manteve as marcas do Planalto ("Incluído pela Lei nº 14.181, de 2021") dentro da transcrição do CDC 54-F, em tensão com C-63; tratar como observação até reaparecer. Origem: APC 0711608-24, onde a minuta trazia só o §§ 2º e 4º do 54-F e Marcos acrescentou o caput, o CDC 7º e 25 e o CC 265 em blocos.

## H. Arquivo e entrega

**C-70 · Nome do arquivo** — ATIVA · todas · v2
Mesmo nome da minuta com "Marcos" após o identificador do assessor (`8 APC 0701708-20 ACA DPP ….docx` → `8 APC 0701708-20 ACA Marcos DPP ….docx`). Sem sufixo "_revisado". A sigla de resultado só muda se o sentido mudou, com fundamentação e comunicação expressa.

**C-71 · Portão de entrega** — ATIVA · todas · v2, v3, v4, v6
Antes de entregar: DOCX íntegro e abrindo; cabeçalho e autuação iguais ao original; modelos, manual e estrutura pronta consultados; coerência ementa-relatório-voto-dispositivo; premissas com ID; citações conferidas; parágrafos verificados no PDF renderizado; fontes, recuos (4 cm; transcrições 4/6; ementas 4), itálicos, títulos, negritos e realces; resumo em vermelho (C-39); sentença em verde (C-45); comentários ancorados e sem decisão deixada ao assessor (C-54); RELATÓRIO no topo; comentários de honorários; separação prova/conclusão na ementa. O `checar_voto.py` v6 verifica a maior parte disso. Em lote, só iniciar a minuta seguinte depois de aprovar a anterior. **v16:** nos EMD, conferir no PDF que a ementa do acórdão embargado foi de fato transcrita no relatório (na EMD 0705293-30 a minuta saiu sem ela, por falha na montagem, e Marcos a acrescentou, completa, em Arial 13 itálico, recuo 4 cm, entre aspas e com o ID ao final).

---