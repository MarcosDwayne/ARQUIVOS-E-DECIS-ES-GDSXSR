# CALIBRAÇÕES — FORMATAÇÃO E ENTREGA DO DOCX (todas as classes) — ASSESSOR GDSXSR

Seção E do núcleo (C-40 a C-48), separada na otimização de 24/10/2026 para ser lida **na Etapa 4** (edição técnica do DOCX) e na conferência do portão, não ao iniciar a revisão. O conteúdo das regras não mudou. Soma-se ao núcleo; hierarquia em conflito e status como no núcleo. Fonte de formatação continua a estrutura pronta da classe (Drive) e o MANUAL ATUALIZADO (C-05).

---
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
Azul e vermelho são do Desembargador (azul: o que vai ler na sessão; vermelho: o que discorda); o revisor não os usa, salvo o resumo de C-39. Jurisprudência em sentido contrário ao voto vai **ao final, em violeta 800080**, sinalizada em comentário no início do documento; parecer da Procuradoria em sentido contrário, ao final, em laranja C45911. O bloco violeta se intitula "PRECEDENTES CONTRÁRIOS AO VOTO" e traz, de cada acórdão, a ementa íntegra e a linha de identificação ("Acórdão n., processo, Relator(a), Turma, data de julgamento, publicado no DJe"), de preferência os mais recentes das Turmas que divergem. **v32 (observada, AGI 0740064-34):** com a decisão recorrida em verde (C-45) e a jurisprudência contrária em violeta, o bloco violeta vem **depois** da decisão recorrida, como último bloco do documento (a minuta vinha com o violeta antes; Marcos inverteu). Observada uma vez, motivo não declarado.

**C-48 · Espaços de colagem do PJe na transcrição da sentença** — ATIVA · todas · v37 · observada em um caso
Na transcrição da sentença ou de outra peça, o número do parágrafo é seguido de **um só espaço** ("45. Da análise…"), e não da sequência de espaços que o PJe deixa na colagem ("45.           Da análise…"). O revisor normaliza os espaços (rastreado, sem mudar palavras) e deixa a transcrição literal quanto ao texto (C-66). Motivo inferido da versão final (Marcos, APC 0703009-02; o assessor não o declarou); a normalização valeu para os parágrafos da sentença no voto (45 a 54), e o relatório da mesma minuta, com defeitos como "3.Tece", não foi alterado por Marcos.
