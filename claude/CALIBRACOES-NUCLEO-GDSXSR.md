# CALIBRAÇÕES — NÚCLEO (todas as classes) — ASSESSOR GDSXSR

**Versão:** v29 · **Data-base:** 23/10/2026 · v29 ajusta C-16, C-20, C-35, C-61 e C-66 e acrescenta, no arquivo da APC, C-3S e C-3T (versão final da APC 0711066-98). v28 acrescenta C-73 (orientação de modelo por classe). v27 é uma poda de tamanho (nenhuma regra vigente mudou de sentido) e acrescenta o limite de tentativas a C-72. Quem corrigiu, em qual processo e o texto integral anterior de cada regra estão em `historico/backup-2026-10-17/pre-poda/` e `historico/REGISTRO-ALTERACOES-CALIBRACOES.md`.
**Onde está o quê:** este arquivo traz as regras de APC, AGI e EMD. Regras de uma só classe estão em `CALIBRACOES-APC-GDSXSR.md`, `-AGI-` e `-EMD-` (ler só a da classe da minuta). Observações ainda não promovidas a regra: `historico/OBSERVACOES-NAO-REGRA-ate-v26.md` (não ler em revisão comum).
**Novas calibrações** entram pela skill `registrar-calibracao`: regra geral aqui, regra de classe no arquivo da classe, "Origem" e linha da versão no registro. Escrever a regra enxuta (enunciado, exemplo mínimo, exceção); o caso que a originou vai ao registro, não aqui.
**Hierarquia em conflito:** instrução do usuário para a minuta atual → regra mais recente e específica → MANUAL ATUALIZADO e estruturas prontas do Drive (formatação) → perfis de estilo → modelos do Drive.
**Status:** ATIVA · SUBSTITUÍDA (só no histórico) · ESPECÍFICA (só para a matéria indicada).

---

## Sumário

A. Princípios · B. Parágrafo e cadência · C. Referências e voz · D. Estrutura · E. Formatação · F. Comentários laterais · G. Jurisprudência e legislação (inclui C-66, citação literal, e C-72, conferência) · H. Arquivo e entrega

---

## A. Princípios

**C-01 · Objetivo de estilo** — ATIVA · todas
O voto não deve parecer escrito por IA. Prioridade: clareza → fidelidade → naturalidade → fluidez → concisão moderada. Pergunta final: "parece escrito ou aperfeiçoado por alguém do Gabinete?". O estilo do Gabinete é o bom senso: citar quando for necessário e relevante para a compreensão, a clareza e a força persuasiva, e evitar excesso e poluição visual (C-66).

**C-02 · Concisão 8 a 8,5, efetiva** — ATIVA · todas
Grau vigente 8 a 8,5 (Marcos, 13/10/2026); a referência "7/10" está superada. Eliminar redundância, repetição de premissa ou conclusão, metalinguagem, duplicação de alegações e transcrição dispensável, sem meta percentual. Não omitir argumento capaz de alterar o resultado, ressalva probatória, distinção de precedente, cálculo, identificação documental ou limite do dispositivo. A concisão tem de aparecer no resultado: o revisor corta, não só reorganiza (meta indicativa: −10% a −20% de palavras sobre a primeira revisão, sem fragmentar, C-13). A transcrição exigida por C-66 não é "transcrição dispensável"; o corte recai sobre o excesso. Cortes típicos: cabeçalho das ementas transcritas (C-62); mini-dispositivo do último capítulo (C-3A); "Tese de julgamento" sem tese nova (C-37); parágrafo que só repete a sentença transcrita; enfrentamento de precedentes em bloco, sem um parágrafo por acórdão. Técnica preferida: fundir parágrafos consecutivos de uma só ideia, suprimir o que antecipa a conclusão do capítulo e qualificações acessórias ("veiculada nas contrarrazões", "como defesa indireta").

**C-03 · Fidelidade** — ATIVA · todas
Não alterar fatos, pedidos, provas, valores, datas, fundamentos essenciais ou resultado por estilo. Não presumir prova ausente nem transformar narrativa de peça em fato incontroverso. Revisar ementa, relatório, voto e dispositivo em conjunto.

**C-04 · Preservação do original** — ATIVA · todas
Trabalhar sobre cópia; registrar hash. Preservar cabeçalho, logotipo, tabela de autuação, margens, cores, comentários anteriores, realces, resumos de trabalho e peças anexadas. Nunca reconstruir o documento a partir da ementa.

**C-05 · Autoridade de estilo × autoridade jurídica** — ATIVA · todas
Modelos do Drive definem forma, estrutura, cadência e prática; fontes oficiais atuais definem lei e jurisprudência vigentes; o modelo não prova fato do processo revisado. Consultar 3 a 8 modelos (OURO → corrigidos/alterados/liberados pelo Desembargador → "Marcos" → mesma classe e resultado → mesma matéria → corpus geral). Minuta não aprovada não vira MODELO OURO. A formatação segue o MANUAL ATUALIZADO e a estrutura pronta da classe (pasta de estruturas do Drive, id 1aEgy58IgkjNOvu0zAYhREeOXViIZeUHI): ler as duas antes de revisar.

## B. Parágrafo e cadência

**C-11 · Um período por parágrafo no voto** — ATIVA · todas, sobretudo APC
Padrão: um período por parágrafo, de cerca de 20 a 45 palavras. Premissa ou regra seguida de período autônomo (conclusão, aplicação, reforço): o segundo ganha parágrafo próprio. Dois períodos juntos só quando o segundo não se sustenta sozinho.

**C-12 · Limite de 4 linhas renderizadas** — ATIVA · todas
Parágrafo editorial com mais de 4 linhas no DOCX renderizado é cindido no ponto lógico, por quebra real de parágrafo, sem dividir oração. Contagem de palavras serve só para triagem. Exceções: parágrafo único de alegações enumeradas; transcrições.

**C-13 · Vedação de fragmentação** — ATIVA · todas
Três ou mais parágrafos livres seguidos com menos de 15 palavras exigem revisão. Exceções: títulos, "Com razão./Sem razão./Com parcial razão.", admissibilidade, "É o relatório.", "É como voto.", mini-dispositivo, dispositivo e transcrições.

**C-14 · Cadência e arquitetura por classe** — ATIVA
Linha de dados do voto ("Ação ajuizada em… Valor da causa"): só na APC (C-3C). APC: discursiva, articula fato, prova, norma, precedente e consequência (perfil APC). AGI: direto, aderente à decisão agravada e à liminar do Relator — manter as razões, reconhecer a probabilidade já vista ou refluir em cognição exauriente (perfil AGI). EMD: relatório curto (ementa do acórdão + uma linha sobre os vícios), um capítulo por vício, com o trecho do acórdão que o enfrentou; prequestionamento e efeitos infringentes só se suscitados (perfil EMD).

**C-15 · Sinais de texto artificial a eliminar** — ATIVA · todas
Série de parágrafos de uma linha; mesma construção repetida; frases conclusivas soltas ("Assim.", "Logo."); reapresentação de fundamento já demonstrado; conectores decorativos; esquema "tese → explicação → conclusão" idêntico em todos os capítulos; excesso de títulos. Exceção: nos EMD as fórmulas fixas de confronto ("A alegação de omissão não merece prosperar…", "O v. acórdão embargado, portanto, cumpriu sua finalidade…", "Na verdade, ao alegar…") são padrão da casa, acompanhadas do trecho do acórdão que as sustenta.

**C-16 · Encadeamento entre parágrafos** — ATIVA · todas
Quando parágrafos curtos passam de um fundamento a outro, abrir com conector que marque a passagem: "Decerto," (reforço), "Por outro lado," (fundamento distinto), "No mais," (último ponto, C-23). "Além disso," também cede a "No mais,"; a tese de tema que traz fundamento distinto abre com "Por outro lado, registro que o STJ, no julgamento do Tema Repetitivo 972, fixou a seguinte tese:", e a norma, com "E, quanto à venda casada, dispõe o art. 39, I, do CDC:" (Marcos, APC 0711066-98, v29). Um conector por parágrafo, sem rodízio mecânico.

## C. Referências e voz

**C-20 · ID e dispositivo legal ao final do período** — ATIVA · todas
Forma compacta entre parênteses: (ID 84771203), (CPC 300), (CPC 373 I; ID 84771203). Evitar "Nos termos do art. …" e "A perícia (ID …) concluiu…". Transcrições literais ficam intactas. A norma transcrita (C-66) é identificada na frase que a introduz ("O art. 373, I, do CPC dispõe:") ou, ao final, entre parênteses depois das aspas — "(CPC 373 I)". Fórmulas fixas do relatório ("Apelo da autora, NOME (ID …), em que alega…"; "Contrarrazões (ID …), em que…") e do dispositivo ("(CPC 85 § 11), acrescido…") não se deslocam. A forma compacta vale na ementa: "(CPC 1.022)", "(CPC 489 § 1º IV)", "(CC 884)", "(LINDB 20)", sem "art." e sem vírgula depois da sigla; nas fórmulas fixas da ementa de EMD, "CPC 1022" e "CPC 1025" ficam sem ponto (C-3J). ID de peça dos autos de origem (e não do agravo) leva a indicação: "(ID 284303352, do processo de origem)". Na APC, os IDs citados na redação do voto são os do PJe de 2º grau (série 8695…, a mesma dos apelos e da sentença no recurso); os IDs de 1º grau (série 1616…), que vêm do relatório da sentença, só ficam dentro da transcrição. Sem acesso ao PJe, o revisor deixa comentário de pendência (C-52) em vez de trocar de memória. Observada em um caso (Marcos, APC 0711066-98, v29: planilha, extratos e contrato).

**C-21 · A minuta nunca é fonte** — ATIVA · todas
Toda afirmação de fato ou prova remete a ato, documento ou ID dos autos. Vedado "a minuta aponta", "a revisão demonstrou" e semelhantes na voz do julgador.

**C-22 · Nome do juiz sentenciante** — ATIVA · todas
Forma exata confirmada no PJe, sem completar nem acrescentar partículas ("Itamar Dias Noronha", não "… Filho"). Se a sentença não identificar o juiz, comentário de conferência.

**C-23 · "No mais" em vez de "ademais"** — ATIVA · todas
"No mais" acrescenta o último elemento. Preferir o pretérito perfeito ao mais-que-perfeito sintético ("já foi arguida", não "já fora arguida"). O manual veda "ademais", "outrossim", "destarte", "porquanto", "mormente", "inobstante", "restou comprovado" (usar "está comprovado"). "No caso," abre o parágrafo que aplica a premissa ao caso ("No caso, essas questões já foram…"), também no lugar de "Na espécie".

**C-24 · Sem inteiro teor** — ATIVA · todas
Conferir apenas o que o material recebido reproduz; declarar a limitação em comentário e no relatório de entrega. Ponto decisivo sem suporte documental impede considerar a minuta pronta para liberação.

**C-25 · "ID" no singular e sem ponto** — ATIVA · todas
Também com vários documentos: "(ID 90523912 e 90523913)", nunca "(IDs …)" nem "ID." (manual, 2.3.3).

**C-26 · Mudança de entendimento do Relator fica no comentário** — ATIVA · todas
O voto não narra que o Relator refluiu de entendimento adotado em outros processos; o parágrafo é suprimido e a divergência com a linha anterior fica só no comentário lateral (C-53). Não vale para o refluxo em relação à própria liminar do processo (perfil AGI, "Reexaminando a controvérsia em cognição exauriente…").

**C-27 · Vocabulário** — ATIVA · todas
(a) Cumprimento de sentença é fase, não ação: "Cumprimento de sentença proposto por…" (não "Ação de cumprimento de sentença proposta…"). (b) "cônjuge" é masculino: "o cônjuge", "bens do cônjuge"; para indicar a mulher, "o cônjuge virago". (c) Ao resumir a decisão agravada, suprimir "por ora" ("que indeferiu o bloqueio", não "que indeferiu, por ora, o bloqueio"). (d) Ao apontar o erro do julgado embargado, "dispositivo do acórdão", não "dispositivo do voto condutor" (caso único). (e) Em cumprimento de sentença, quem executa é o "exequente", e não "autor", na ementa e no dispositivo.

## D. Estrutura

**C-30 · Alegações enumeradas em parágrafo único** — ATIVA · todas
No relatório e no voto, as alegações de cada parte e manifestação ficam em um só parágrafo, com 1), 2), 3)…, mesmo acima de quatro linhas, com o ID ao final. Acrescentar a enumeração quando faltar, sem omitir nem inventar fundamentos. Não se aplica a transcrições. Números em negrito (C-43).

**C-31 · Relatório sem "Requer o não provimento do recurso." nem "Preparo recolhido"** — ATIVA · todas
Suprimir a fórmula após as contrarrazões; o "Requer …" do recorrente continua em parágrafo próprio. Também sai "Preparo recolhido (ID …)" depois do pedido do recorrente; preparo só aparece quando for ponto do julgamento (deserção), no capítulo de admissibilidade.

**C-32 · RELATÓRIO no topo da página** — ATIVA · todas
O título começa no topo da página seguinte ao fim do bloco anterior (ementa ou resumo, C-39), sem parágrafos vazios excedentes. Conferir no PDF.

**C-33 · Ementa espelha o voto** — ATIVA · todas
Não introduzir na ementa prova, tese ou resultado ausente do voto. Classificação, número de recursos e comando final coincidem. Ao cortar parágrafo do voto, a ementa (itens, renumeração do dispositivo e rodapés "Dispositivos relevantes citados" e "Jurisprudência relevante citada") acompanha.

**C-34 · Ementa, item 1: "pessoa natural"** — ATIVA · todas
Qualificar a parte autora pessoa física como "pessoa natural" ("Ação proposta por consumidor pessoa natural contra …"). Quando a ação tem nome próprio (embargos de terceiro, mandado de segurança), o item 1 começa por ele, sem "Ação de"; ação comum mantém ("Ação de cobrança de valores…"). O item 1 não leva data de ajuizamento, valor da causa, juízo ou vara: isso fica na linha de dados (APC) e no relatório. No cumprimento de sentença coletiva, acrescenta entre parênteses o número da ação coletiva de origem ("… expurgos inflacionários em cadernetas de poupança (Ação Civil Pública nº 1998.01.1.016798-9).").

**C-34A · Ementa, item 1: partes nomeadas e elementos que a tornam clara** — ATIVA · todas (revisão e minuta do zero)
Orientação do Des. Sérgio Rocha, via Marcos (15/10/2026). O item 1 **sempre** nomeia as partes (autor e réu; agravante e agravado; embargante e embargado; apelante e apelado):
(a) **Pessoa jurídica:** nome literal da autuação ("Banco do Brasil S.A.", "Distrito Federal"), sem sigla genérica nem "empresa", "instituição financeira" ou "ente público" no lugar do nome.
(b) **Pessoa física:** não se usa o nome civil; qualifica-se como **pessoa natural** (C-34), acrescentando, sempre que possível e conforme os autos, o que esclareça a ementa: idade e condição ("menor, com 7 anos de idade", "idoso, com 78 anos"); doença ou deficiência, com o nome ("portadora de transtorno do espectro autista", "com síndrome de Down"); condição profissional ou de consumidor quando relevante.
(c) **Papel processual por matéria:** inventário e partilha: inventariado, inventariante, herdeiro(s), meeiro, cônjuge supérstite; divórcio e união estável: cônjuge virago e varão (ou companheira e companheiro); alimentos: alimentando, alimentante, genitor, genitora, guardião; cumprimento de sentença: exequente e executado; tutela e curatela: curador, curatelado, tutor, tutelado; e assim nas demais matérias.
(d) **Só o que consta dos autos e interessa ao julgamento:** idade, doença e deficiência vêm dos autos (ID ao conferir), nunca presumidas; dado sensível que nada acrescente fica de fora. A lista é exemplificativa (gestante, militar, servidor, consumidor idoso, pessoa em recuperação judicial etc.).
Exemplo: "1. Ação de alimentos proposta por menor, com 9 anos de idade e portadora de síndrome de Down, representada pela genitora, pessoa natural, contra o genitor, pessoa natural, que busca majorar a pensão…". Continuam valendo C-34 e C-33.

**C-35 · Ementa, "III. Razões de decidir": um fundamento por item** — ATIVA · todas
Prova em um item, consequência jurídica em outro; item que reúne premissa geral e aplicação ao caso é cindido em dois (p. ex., "Inexiste omissão quando o acórdão aprecia…" e "As matérias apontadas… (CPC 505 I)"; omissão e contradição em itens separados). **Na APC vale C-3G (v29):** o item reúne a regra e a aplicação ao caso, sem desdobrar prova e conclusão. Renumerar todos os itens depois, inclusive "IV. Dispositivo".

**C-36 · Ementa numerada em sequência, inclusive o item 3** — ATIVA · todas
Mantida por Marcos em 13/10/2026: todos os itens de I a IV levam número seguido de ponto, também o item 3 de "I. Caso em exame" (razões do recurso): "3. A autora apelou sustentando…". Perfis antigos que dizem "sem enumeração" estão superados.

**C-37 · Sem "Tese de julgamento" na ementa** — ATIVA · todas, salvo tese nova
A estrutura pronta não a prevê. Suprimi-la quando o voto apenas aplica tese já firmada (tema repetitivo, súmula) ou mantém a sentença; manter só se o voto fixar entendimento novo, e então com comentário.

**C-38 · Fórmula preliminar + mérito** — ATIVA · todas
Havendo preliminar, ementa e dispositivo usam "e, no mérito,": "Rejeitou-se a preliminar de não conhecimento e, no mérito, negou-se provimento ao apelo da autora." / "Ante o exposto, **rejeito** a preliminar … e, no mérito, **nego provimento** ao apelo…". Alegação não conhecida: "não conheço da alegação de prescrição, veiculada nas contrarrazões, e, no mérito, nego provimento…". Conferir ementa, voto e dispositivo juntos.

**C-39 · Resumo do recurso em sentido contrário ao voto** — ATIVA · APC, AGI, EMD
Entre a ementa ("Jurisprudência relevante citada") e o RELATÓRIO vai o bloco de trabalho do resumo (na estrutura pronta, "RESUMO COPILOT"), em **vermelho EE0000**, Arial 14:
- título "RESUMO DA APELAÇÃO EM SENTIDO CONTRÁRIO AO VOTO" (AGI: "DO AGRAVO"; EMD: "DOS EMBARGOS"), em negrito e realçado em amarelo;
- "I. RAZÕES RECURSAIS" em negrito; para cada tese do recorrente, subtítulo em negrito e parágrafo-síntese numerado (lista automática 1., 2., 3.…), na voz do recorrente ("A apelante sustenta…", "Alega…");
- "II. PEDIDO" em negrito e o pedido em um parágrafo.
Serve para o Desembargador ver o melhor argumento contrário. Se a minuta não o tiver, o revisor o insere (rastreado), com base nas razões recursais dos autos. É a única exceção ao cinza de C-44 e à reserva do vermelho (C-46).
**Voto que dá provimento e cassa ou reforma a sentença:** o resumo em vermelho é o da **sentença**: título "RESUMO DA SENTENÇA EM SENTIDO CONTRÁRIO" (sem "AO VOTO"); "I. RAZÕES DE DECIDIR", com subtítulo por fundamento e parágrafo numerado na voz do juízo ("O juízo consignou…", "A sentença reconheceu…"); "II. DISPOSITIVO DA SENTENÇA" com o dispositivo e as determinações finais. Contrarrazões não entram. É o padrão do perfil AGI ("RESUMO DA DECISÃO EM SENTIDO CONTRÁRIO") estendido à APC. O portão `checar_voto.py` reconhece os títulos iniciados por "RESUMO DA APELAÇÃO", "DO AGRAVO", "DA DECISÃO", "DA SENTENÇA" e "DOS EMBARGOS".

**C-3A · Mini-dispositivo de capítulo** — ATIVA · todas
Cada capítulo, exceto o último, termina com a conclusão sublinhada e realçada em amarelo ("Rejeito a preliminar." / "Assim, nego provimento ao apelo, nesse ponto." / "Dou provimento ao apelo, nesse ponto, para…"), com vírgula antes de "nesse ponto" também no AGI ("Assim, nego provimento ao agravo de instrumento, nesse ponto."). No último capítulo, ou em tópico único, não há mini-dispositivo: o voto segue direto para o DISPOSITIVO. EMD: quando o capítulo acolhe os embargos, indica a finalidade ("Assim, dou provimento aos embargos de declaração, nesse ponto, sem efeitos infringentes, para sanar a obscuridade e erro material existentes."; caso único, mantida a brevidade para o não acolhimento).

**C-3F · Dispositivo em parágrafo único** — ATIVA · todas
O DISPOSITIVO é um parágrafo; a determinação consequente entra na mesma frase por "a fim de que", e não em segundo parágrafo iniciado por "Determino" ("…dou provimento ao agravo de instrumento das exequentes, … para confirmar a liminar, a fim de que o novo edital de leilão, com as retificações já definidas na origem, seja expedido…"). Decisão distinta e autônoma — gratuidade de justiça recursal, fixação ou redistribuição de honorários e ônus — vai em parágrafo próprio, nesta ordem: resultado do recurso; gratuidade; honorários e ônus ("Sem honorários recursais (CPC 85 § 11)."). Ver C-3Q (APC).

## E. Formatação

**C-40 · Fontes** — ATIVA · todas
Arial 14 no texto editorial (ementa, relatório, voto, títulos, dispositivo). Transcrições (sentença, documentos, alegações, ementas, lei, tese) em **Arial 13 e itálico**, entre aspas; aspas internas viram simples. Na ementa, os rótulos "Dispositivos relevantes citados:" e "Jurisprudência relevante citada:" em itálico (só o rótulo). Não aplicar Arial 13 nem itálico aos anexos.

**C-41 · Página, espaçamento e recuos** — ATIVA · todas
- Página A4; margens superior e inferior 2,5 cm, esquerda e direita 3 cm.
- Texto normal: justificado, entrelinha 1,5, 0 pt antes e depois, **recuo de primeira linha 4 cm** (não 2,54), um parágrafo vazio entre parágrafos normais.
- Transcrição de sentença, documento ou alegação: **recuo esquerdo 4 cm e primeira linha em 6 cm**, sem parágrafo vazio interno. Citação dentro de transcrição: recuo 6 cm, inclusive a primeira linha.
- Ementa transcrita e texto de lei: recuo esquerdo 4 cm, **sem** recuo de primeira linha. Tese de tema transcrita: como trecho (4 cm / 6 cm).
- Títulos e subtítulos sem recuo de primeira linha; "O Senhor Desembargador SÉRGIO ROCHA – Relator." sem recuo.

**C-42 · Títulos** — ATIVA · todas
Títulos e subtítulos da ementa sempre à esquerda (EMENTA, I a IV); "EMENTA" em negrito. Entre RELATÓRIO e DISPOSITIVO, títulos e subtítulos de fundamentação centralizados. Título do recurso em negrito; subtítulo de capítulo sem negrito, antecipando o resultado ("DA REJEIÇÃO DA PRELIMINAR DE…") e **realçado em amarelo**; DISPOSITIVO em negrito. O veredito isolado ("Sem razão.", "Com razão.") também em amarelo.

**C-43 · Ênfases** — ATIVA · todas
- Relatório e voto: números da enumeração das alegações — 1), 2), 3)… — em **negrito** (manual 2.3.5); o nome da parte no "Apelo da autora, NOME (ID …)" **sem** negrito.
- Mini-dispositivo de capítulo sublinhado e em amarelo (C-3A).
- Dispositivo: negrito no núcleo decisório (**rejeito**, **nego provimento**, **dou parcial provimento**) e no verbo de honorários (**Condeno**, **Majoro**).
- Realce amarelo com parcimônia, nunca em transcrições inteiras. Além de subtítulos, vereditos e mini-dispositivos, realçar em cada capítulo os 2 a 4 períodos que decidem a questão — a premissa jurídica decisiva, o fato provado (ou não provado) que a resolve e a conclusão ("Essa possibilidade não equivale à prova do nexo causal…"); em EMD, o fundamento do acórdão, o ponto não enfrentado, o fato central com ID. Realça-se a frase que fixa a premissa e a que enuncia a conclusão, não o parágrafo todo. Não realçar alegações, relatório, transcrições inteiras nem parágrafos de passagem.
- Dois parágrafos curtos seguidos que se completam são fundidos em um (C-11/C-13).
- A cor das alterações do revisor segue C-44.

**C-44 · Controle de alterações com texto em cinza** — ATIVA · todas (instrumento interno; a entrega é C-47)
Toda alteração do revisor é rastreada (autor "Assessor GDSXSR"): inserções em w:ins, exclusões em w:del, cisões com a marca de parágrafo inserida, recuos e alinhamento em w:pPrChange, negrito/itálico/tamanho/realce/sublinhado em w:rPrChange. O texto inserido vai em 808080, de modo que, **aceita a alteração, permanece cinza**; o excluído some. Texto original não alterado conserva a cor própria. Parágrafo com comentário também é reescrito (as âncoras são preservadas pela ferramenta); só parágrafo com campo, hiperlink, nota ou imagem fica protegido. Única exceção de cor: o resumo em vermelho (C-39).

**C-47 · Entrega com alterações já aplicadas, em cinza, só com comentários** — ATIVA · todas
Confirmada por Marcos em 13/10/2026. O assessor não aceita nem rejeita alteração por alteração. O revisor edita com `revisao_tracked.Revisor` (para o portão `checar_voto.py` conferir) e **entrega o DOCX com todas as alterações do autor "Assessor GDSXSR" já aceitas** (`aceitar_autor.py`, que aceita só as marcas do revisor): texto novo em cinza 808080 (resumo em vermelho, C-39), excluído desaparece, cada alteração relevante explicada em comentário lateral (C-54/C-55). A cópia rastreada fica só em `entregas/rastreados/`. Alterações rastreadas de terceiros já existentes na minuta são preservadas, e o portão acusa inserção "sem cinza" apenas por elas — justificar no relatório.

**C-45 · Decisão recorrida anexada em verde** — ATIVA · todas
A sentença (ou decisão agravada, ou acórdão embargado) vai ao final, depois de "É como voto.", inteira em **verde 00B050**; as partes principais podem ser realçadas (manual: "realçando em marrom as partes principais").

**C-46 · Cores reservadas e blocos finais** — ATIVA · todas
Azul e vermelho são do Desembargador (azul: o que vai ler na sessão; vermelho: o que discorda); o revisor não os usa, salvo o resumo de C-39. Jurisprudência em sentido contrário ao voto vai **ao final, em violeta 800080**, sinalizada em comentário no início do documento; parecer da Procuradoria em sentido contrário, ao final, em laranja C45911. O bloco violeta se intitula "PRECEDENTES CONTRÁRIOS AO VOTO" e traz, de cada acórdão, a ementa íntegra e a linha de identificação ("Acórdão n., processo, Relator(a), Turma, data de julgamento, publicado no DJe"), de preferência os mais recentes das Turmas que divergem.

## F. Comentários laterais

**C-50 · Comentário jurídico com texto literal** — ATIVA · todas
Em ementa, relatório e voto, quando houver ponto jurídico ou probatório: trecho literal da lei ou tese, identificação precisa, fonte oficial e providência concreta (ID a conferir, efeito de resultado contrário). Referência solta ("CPC 371", "Tema 972") é insuficiente. Distinguir literal de paráfrase. Preservar comentários anteriores. O texto que C-66 manda levar ao corpo não se repete no comentário; a norma ou tese fora do corpo tem o texto literal no comentário (C-63).

**C-51 · Comentários de honorários no dispositivo** — ATIVA · todas
Ao fixar ou majorar honorários recursais: comentário em "valor (atualizado) da causa" com o valor; comentário em "r. sentença" com a transcrição literal do capítulo de custas e honorários (percentual, base, dispositivos, suspensão por gratuidade). O percentual é decisão do Relator, não regra: manter a proposta (p. ex. 2%) com o comentário. A suspensão se escreve nomeando a gratuidade: "suspensão da exigibilidade pela concessão da gratuidade de justiça (CPC 98 § 3º)".

**C-52 · Comentários de pendência** — ATIVA · todas
Pendência só para o que **não** pode ser conferido com o material disponível (fato fora dos autos recebidos, documento ilegível). O que o revisor pode conferir, ele confere e corrige. São instrumento de trabalho: o assessor os apaga ao resolver; os de conteúdo normativo literal permanecem na versão final.

**C-53 · Divergência com a linha decisória** — ATIVA · todas
O revisor não altera o **resultado** (C-03). Divergência da linha do Gabinete vai para comentário, com o modelo de referência e o fato que a justificaria. Jurisprudência contrária relevante (inclusive a invocada pela parte) não fica como pergunta, e o revisor **não escreve parágrafo de distinção do precedente contrário**: ela vai só ao final, em violeta (C-46), com comentário que diz o que fez, e não entra em "Jurisprudência relevante citada" da ementa. Ver C-68.

**C-54 · O revisor altera, não sugere** — ATIVA · todas
Toda melhoria identificada é **feita no texto** (em cinza, rastreada, C-44) — inclusive em parágrafos com comentário, fórmulas, linha de dados, ementa e dispositivo —, e cada alteração relevante recebe comentário lateral curto que diz **o que foi alterado e por quê**, com a regra aplicada: "ASSESSOR GDSXSR — Alterei 'Recurso interposto' para 'Apelo interposto' … conforme a estrutura pronta APC (C-54)." Proibido deixar a decisão ao assessor ("Sugestão…", "Sugiro…", "Decidir se…", "Avaliar se…", "a critério"). Limites: não mudar o resultado (C-03/C-53) nem fato sem prova nos autos (C-24).

**C-55 · Comentário diz o que foi feito** — ATIVA · todas
Comentários são a comunicação com o Desembargador: concisos, pertinentes, sobre o que foi alterado e os pontos sensíveis (manual 2.3.9). Alterações de mesma natureza (recuos, itálicos, IDs) recebem um único comentário geral no início do documento.

## G. Jurisprudência e legislação

**C-60 · Confirmação em fonte oficial** — ATIVA · todas
Legislação: Planalto; SINJ/DF (DFLegis auxiliar). Jurisprudência: JurisDF, SCON/STJ, STF; Dizer o Direito só para descoberta. Acórdão isolado não é tese qualificada. Citação não confirmada é retirada ou sinalizada em comentário. Modelo antigo não torna vigente o que cita. O registro do iajus pode estar defasado: se disser "pendente" ou "sem tese", o revisor não o afirma no voto sem conferir o andamento no site do tribunal (ou declara em comentário que não conseguiu); o inteiro teor enviado pelo usuário prevalece sobre o registro (ex.: Tema 1.230/STJ, julgado no REsp 1.894.973/PR, DJEN de 21/9/2026, quando o iajus ainda o dava como pendente). Método: "não localizado" só depois de busca estreita no iajus — órgão julgador exato, data de julgamento nos últimos 12 meses e termos do ponto —, lendo todo resultado grande com jq; a busca ampla ranqueia julgados antigos e a lista salva deve ser lida até o fim.

**C-61 · Tese de tema transcrita literalmente** — ATIVA · todas
Quando o voto se apoia em tema repetitivo ou de repercussão geral (STJ ou STF), a tese é transcrita literalmente, em parágrafo de transcrição (C-40/C-41), introduzida por "O c. STJ, no julgamento do Tema Repetitivo 1.085, fixou a seguinte tese:" e seguida do leading case no formato oficial: "(REsp n. 1.863.973/SP, relator Ministro Marco Aurélio Bellizze, Segunda Seção, julgado em 9/3/2022, DJe de 15/3/2022.)". Não parafrasear a tese. Aplica-se requisito a requisito, em parágrafos curtos ("Quanto ao requisito (a)…"; "No mais, quanto ao requisito (b)…"), e a ementa cita o tema na rubrica da jurisprudência ("REsp nº 1.894.973/PR (Tema 1.230)"). Orientação do Des. Sérgio Rocha (Marcos, 14/10/2026). Vale para todo tema citado no corpo, inclusive o que apoia ponto acessório: "Nesse sentido, a Segunda Seção do c. STJ, no julgamento do REsp n. 1.061.530/RS (Tema 24), submetido ao rito dos recursos repetitivos:" + tese entre aspas. Não basta deixar a tese em comentário C-63 (Marcos a trouxe para o corpo na APC 0711066-98, v29).

**C-62 · Ementa de precedente transcrita sem cabeçalho** — ATIVA · todas
Na citação de jurisprudência, suprimir o cabeçalho (verbetação em caixa alta) e os itens irrelevantes; a transcrição começa com "“(...) " no mesmo parágrafo do primeiro item aproveitado ("“(...) 2. Nos termos do Tema 1.085 do STJ…"), sublinhando o mais importante, e termina com a origem: "(Acórdão n., processo, Relator(a): NOME, Nª TURMA CÍVEL, data de julgamento: …, publicado no DJe: ….) – Grifei". Ponto final depois de "(...)" quando o corte interrompe a frase ("pela escrituração contábil (...).”"), sempre dentro das aspas. Exceção: no relatório dos EMD, a ementa do acórdão embargado vai completa.

**C-63 · Comentário com o texto literal de dispositivo, súmula ou tese** — ATIVA · todas
Sempre que o voto (ou a ementa, o relatório e o dispositivo, quando a menção só aparece ali) mencionar dispositivo de lei, súmula ou tese vinculante do STJ ou do STF, o revisor cria comentário lateral que o transcreve **entre aspas**, com identificação precisa e fonte oficial: "ASSESSOR GDSXSR — Texto literal (C-63): CPC, art. 373, I: “Art. 373. O ônus da prova incumbe: I - ao autor, quanto ao fato constitutivo de seu direito;” (fonte: Planalto)". Um comentário por dispositivo, ancorado na primeira menção no voto; vários dispositivos do mesmo período no mesmo comentário. Transcrever só o caput e o inciso ou parágrafo citado (com "(...)"), sem as anotações do Planalto. Não se aplica a dispositivos dentro de transcrições da sentença ou de precedentes. Toda norma, súmula ou tese que **não** for transcrita no corpo — por ser desnecessária ou redundante, ou por aparecer só na ementa, no relatório, no dispositivo ou em fórmula fixa (C-66 (e)) — tem o texto literal no comentário. Quando a transcrição está no corpo, o comentário não a repete.

**C-64 · Conferir a vigência do dispositivo citado** — ATIVA · todas
Ao transcrever (C-63), conferir no Planalto se foi revogado ou alterado. Fato anterior à revogação: manter a norma da época e dizê-lo no texto e na ementa, indicando a norma atual ("CC 786, vigente à época; Lei 15.040/2024 94"); posterior: substituir pela vigente. Comentar a mudança com as datas.

**C-65 · Um precedente por tese; ementa só lista o que o voto usa** — ATIVA · todas, sobretudo AGI
Cada tese recebe um precedente transcrito; cortar o segundo ("No mesmo sentido:" + ementa + "– Grifei") e o parágrafo de "caso semelhante" que só introduz outro acórdão. "Jurisprudência relevante citada" lista apenas os precedentes que continuam no voto. Precedente que o acórdão embargado já citou não é reapresentado com número no voto dos EMD, salvo se for o ponto discutido. Não dispensa a transcrição da tese de repetitivo ou repercussão geral que sustenta o capítulo (C-66). Exceção em C-67 (divergência interna da Turma).

**C-66 · Citação literal no corpo do voto: norma, cláusula, documento e tese** — ATIVA · todas (revisão e minuta do zero)
Orientação do Des. Sérgio Rocha, via Marcos (14/10/2026). Quando o voto se apoia em um destes elementos, o texto literal vai transcrito no corpo, e não apenas citado ou parafraseado:
(a) **Norma:** artigo de lei, decreto, resolução (CNJ, TJDFT) ou outra norma que fundamente o capítulo — caput e inciso, alínea ou parágrafo pertinentes, com "(...)" para o que se omite, sem as anotações do Planalto, na redação vigente à época do fato (C-64). O artigo é transcrito em **um só bloco**, que começa pela cabeça do artigo, seguida de "(...)" em linha própria e do inciso ou parágrafo pertinente; não se cinde por parágrafo legal, e a frase de introdução cita todos ("Dispõe o art. 330, §§ 2º e 3º, do CPC:"), seguindo o padrão de citação de normas do manual. Se o bloco com dois artigos ou incisos passa de 4 linhas (C-12), parte-se em parágrafos de transcrição (cabeça, inciso I, inciso II com "(...)", art. seguinte), mantidos recuo e identificação "(CC 202 I e II e 203.)" no último; na transcrição de artigo único, a identificação entre parênteses é suprimida, porque a frase de introdução já o cita. Súmula e enunciado seguem o mesmo critério.
(b) **Cláusula contratual:** a cláusula (ou o trecho) em que o julgamento se apoia, com o número e o ID do contrato ao final: "Cláusula 8.2: “…” (ID …)." Quando o contrato não veio nos autos recebidos, o revisor deixa a pendência (C-52); a forma que Marcos adotou foi o **print (imagem) do trecho** em parágrafo próprio, depois de "A Cláusula Segunda, Parágrafo Segundo, do contrato impôs o seguro prestamista ao réu, o que configura a venda casada vedada pelo ordenamento (ID …):" e antes do parágrafo que a aplica (APC 0711066-98, v29).
(c) **Documento relevante:** laudo, relatório, auditoria, parecer, nota técnica, extrato, e-mail, ata, trecho da inicial, da defesa ou do recurso quando a conclusão do voto depender dele. Transcreve-se o trecho que sustenta a conclusão, com o ID ao final (e página, item ou número da peça quando houver). Se a conclusão é "o relatório de asseguração aponta regularidade", o trecho do relatório vem transcrito.
(d) **Tese de recurso repetitivo ou de repercussão geral:** tese literal com o leading case, na forma de C-61.
**Como fazer:**
- Parágrafo próprio, entre aspas, formatado conforme C-40/C-41 (documento e cláusula: Arial 13 itálico, 4 cm com primeira linha em 6 cm; lei: 4 cm sem primeira linha; tese: como trecho), introduzido por frase curta que diga o que é e de onde vem; o parágrafo seguinte aplica o trecho ao caso, **sem repeti-lo com outras palavras**.
- O trecho é literal, dos autos ou da fonte oficial (Planalto, SINJ/DF, STJ, STF), nunca de memória. Se o documento não está nos autos recebidos nem na minuta, não se inventa a transcrição: comentário de pendência com a ID a transcrever (C-24, C-52) e o voto não é dado como pronto.
- Em bloco e sem enchimento: só o trecho que sustenta o ponto; vários dispositivos do mesmo tema, ou várias cláusulas conexas, em um bloco só; a mesma norma, cláusula ou tese é transcrita **uma vez**, onde fundamenta pela primeira vez, e depois só referida; trecho longo é cortado com "(...)".
- Transcrição não conta como fragmentação nem como parágrafo longo (C-12, C-13).
(e) **Fora do corpo** (citação compacta, C-20, e texto literal no comentário de C-63): a norma que aparece apenas na ementa, em "Dispositivos relevantes citados", no dispositivo ou em fórmula fixa (honorários recursais "(CPC 85 § 11)", suspensão por gratuidade "(CPC 98 § 3º)", consectários de rotina), a que está dentro de transcrição de sentença ou de precedente, a citada só para identificar a ação ou o recurso, e as fórmulas fixas do relatório. Acórdão comum (que não é tese de repetitivo ou de repercussão geral) segue C-62 e C-65.
**Ponderação (bom senso do Gabinete):** a regra não manda transcrever tudo. Não transcrever o que o voto já diz com a mesma clareza, o que é notório ou pacífico, o que só repete outra transcrição ou a sentença transcrita, nem dispositivos acessórios. Transcrever quando necessário e relevante para a compreensão, a clareza dos argumentos e a capacidade suasória. **O que o revisor deixar fora do corpo por esses motivos continua com o texto literal em comentário lateral (C-63).** Em dúvida, prefira o comentário quando a transcrição apenas confirmar o que o texto já deixa claro. A norma que **sustenta o capítulo central** entra no corpo mesmo quando pacífica (p. ex., a que fixa o prazo prescricional aplicado, CC 206 § 5º I e 206-A, transcrita em bloco único com "(...)"; a frase "As premissas não são controvertidas" sai); a ponderação vale para dispositivos acessórios.
**Reconciliação:** C-02 (concisão) vale sobre o excesso, não sobre a transcrição necessária; C-63 é o lugar do texto literal do que fica fora do corpo; C-61 vale para repercussão geral; C-65 e C-17 (AGI) continuam cortando precedente repetido, de ponto não discutido ou não lido; C-3B continua sem citar artigo na admissibilidade da remessa necessária. Nos EMD, o trecho do acórdão (C-15) é obrigatório e C-66 acrescenta a norma do vício no primeiro capítulo em que fundamenta e os documentos de que dependa a conclusão (restrição em C-3K). Na AGI, a transcrição da liminar e da decisão agravada segue o perfil AGI.

**C-67 · Jurisprudência da Turma: acórdãos recentes no corpo; o do Relator mais antigo no comentário; ementa com identificação completa** — ATIVA · todas (observada em APC)
Para a tese que o Gabinete já firmou, o voto transcreve os acórdãos **mais recentes da 4ª Turma Cível** (de preferência dos últimos 12 meses; a preferência cede quando a tese só está firmada em julgados mais antigos) e abre com "Nesse sentido:" (não "Nesse sentido, o entendimento desta Turma:"), cada um com "– Grifei". Na divergência interna do TJDFT, admite-se mais de um acórdão da Turma para a mesma tese (exceção a C-65). O julgado anterior do próprio Relator **sai do corpo e vai para comentário lateral** iniciado por "Voto de acordo com entendimento anterior:" (ou "Voto conforme entendimento do dr Sergio e 4TC:"), com a ementa literal (par. de C-26); a frase que enuncia a tese ("Esta c. Turma, em caso semelhante, assentou que…") permanece. A tese de tema só afetado também vai em comentário, com a delimitação literal e a ressalva de que não há tese firmada (C-61). Em "Jurisprudência relevante citada" da ementa, cada julgado tem identificação completa: STJ — "REsp nº 1.273.643/PR, Rel. Min. Sidnei Beneti, Segunda Seção, j. 27/02/2013, DJe 04/04/2013, Tema 515"; TJDFT — "Acórdão 2167090, Processo nº 0761962-37.2025.8.07.0001, Rel. Des. Mário-Zam Belmiro, 4ª Turma Cível, j. 19/08/2026, DJe 03/09/2026". Julgado sem número de acórdão ou DJe não entra na ementa sem conferência no JurisDF (C-60).

**C-72 · Escalonamento da conferência, com limite de tentativas: o voto não sai sem conferir** — ATIVA · todas (revisão e minuta) · v26, v27
Determinação de Marcos (16/10/2026); limite de tentativas acrescentado em v27 (17/10/2026). Quando a conferência de norma ou precedente não for possível pelo iajus e pelas skills de plano B, segue, nesta ordem: (1) busca na web (Google ou Bing), até o texto na fonte oficial ou, na falta dela, em fonte confiável que reproduza o acórdão ou a norma; (2) extensão Claude no Chrome (skill chrome-browser), abrindo direto o portal oficial (JurisDF, SCON/STJ, STF, Planalto, SINJ-DF), quando as ferramentas do navegador estiverem disponíveis na thread.
**Limite:** **até 3 tentativas por citação nas vias extras (web e Chrome), somadas** — uma tentativa é uma busca ou abertura de portal com termos novos (processo, relator, órgão, data, tema); repetir a mesma busca não conta como nova, mas também não se repete. Dentro desse limite, a tentativa deve ser dirigida: no Chrome, abrir direto o portal e o número do processo, sem navegar à toa. As vias ordinárias (iajus e plano B) continuam sem limite fixo, mas seguem o método estreito de C-60. Conferida a citação em qualquer tentativa, para-se ali.
**Esgotado o limite sem conferir:** a citação fica **pendente**, em comentário lateral (C-52) que diz em uma linha o que foi tentado (vias e termos) e o que falhou; a thread diz o mesmo em uma linha ao entregar. Nunca entregar citação não conferida como se conferida, nem completar processo, relator, data ou tese de memória; precedente que não se conferiu e não se consegue manter sem fonte é retirado do corpo ou sinalizado (C-60). O voto não sai citando sem conferência: o limite encerra a busca, não dispensa a conferência. O que a web trouxer em fonte não oficial é conferido no repositório oficial sempre que este abrir, e o Dizer o Direito continua só para descoberta (C-60). Vale para as threads novas; as em andamento não releem as instruções, e o Chrome só entra se estiver disponível na thread.

**C-73 · Orientação de modelo por classe (custo em tokens)** — ATIVA · todas · v28
Decisão de Marcos (17/10/2026), como **orientação**, sem troca automática de modelo: **EMD e AGI sem tese nova** (matéria já firmada nas calibrações, nos modelos e na Turma) podem ser revisadas com modelo mais leve; **APC** e qualquer minuta com **matéria controvertida, tese nova, divergência na Turma ou conferência difícil** usam o modelo mais forte. Na dúvida sobre se a tese é nova, usar o mais forte. A escolha não reduz o rigor: portão, conferência (C-72) e calibrações valem igual. A thread não troca de modelo sozinha; quando a classe e a matéria indicarem o modelo mais leve, diz em uma linha ao iniciar, e Marcos decide.

## H. Arquivo e entrega

**C-70 · Nome do arquivo** — ATIVA · todas
Mesmo nome da minuta com "Marcos" após o identificador do assessor (`8 APC 0701708-20 ACA DPP ….docx` → `8 APC 0701708-20 ACA Marcos DPP ….docx`). Sem sufixo "_revisado". A sigla de resultado só muda se o sentido mudou, com fundamentação e comunicação expressa.

**C-71 · Portão de entrega** — ATIVA · todas
Antes de entregar: DOCX íntegro e abrindo; cabeçalho e autuação iguais ao original; modelos, manual e estrutura pronta consultados; coerência ementa-relatório-voto-dispositivo; premissas com ID; citações conferidas (C-72); parágrafos verificados no PDF renderizado; fontes, recuos (4 cm; transcrições 4/6; ementas 4), itálicos, títulos, negritos e realces; resumo em vermelho (C-39); sentença em verde (C-45); comentários ancorados e sem decisão deixada ao assessor (C-54); RELATÓRIO no topo; comentários de honorários; separação prova/conclusão na ementa. O `checar_voto.py` verifica a maior parte disso. Em lote, só iniciar a minuta seguinte depois de aprovar a anterior. Nos EMD, conferir no PDF que a ementa do acórdão embargado foi de fato transcrita no relatório (completa, em Arial 13 itálico, recuo 4 cm, entre aspas e com o ID ao final).

---
