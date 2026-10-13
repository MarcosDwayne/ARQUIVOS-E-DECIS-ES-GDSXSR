# Diagnóstico geral do projeto Revisor GDSXSR — 13/10/2026

Só diagnóstico. **Nada foi apagado, movido ou alterado.** Tudo o que sugiro remover ou mudar depende da sua aprovação, e antes de qualquer mudança faço backup em `historico/backup-AAAA-MM-DD/`, como manda o projeto.

## 1. Resumo em 8 pontos

1. **O maior desperdício de tokens é ler 60 KB de calibrações (~8.800 palavras, ~17 mil tokens) a cada conversa**, e o arquivo cresce a cada rodada. A regra de dividir por classe e por assunto corta isso pela metade ou mais.
2. **As skills citam ferramentas que não existem mais.** `coerencia-turma` e `pesquisar-jurisprudencia` mandam usar `buscar_hibrida`, `buscar_por_cnj`, `obter_texto_acordao`. O iajus hoje oferece `pesquisar_decisoes` (com modos híbrida, textual, CNJ), `pesquisar_precedentes`, `pesquisar_normas`, `consultar_fonte_oficial` e `ler_documento`. A `revisar-voto` cita `sumulas_e_temas`, `decisao`, `buscar_decisoes` e `verificar_citacoes` do conector "Precedentes", e esse conector hoje só expõe ferramentas de peças e licitação. **Isso é o risco nº 1 para erro em conferência de norma e precedente.**
3. **A skill `revisar-voto-gdsxsr` está desatualizada e contradiz as calibrações.** Ela diz "concisão 7/10" e "calibração v6", mas a regra vigente é 8–8,5 (v16). Manda entregar "o arquivo rastreado, não o aceito", o oposto de C-47 e das instruções do projeto. Manda usar `project_read`, que não existe no Claude Code.
4. **O `agente.yaml` também está parado em v6** (concisão 7, calibração v6) e o `PERFIL-ESTILO-GDSXSR-v1.1.md` ainda fixa concisão 7.
5. **Há ~12 cópias idênticas de arquivos e ~200 MB de PDFs na raiz**, mais cópias de `votos-revisados/`, `entregas/` e `historico/` que repetem o mesmo voto em 3 ou 4 lugares.
6. **Os plugins ativos no repositório (claude-mem, headroom, cartographer, claude-code-setup) não servem a este trabalho** e consomem contexto e tokens.
7. **Faltam as peças que as instruções do projeto citam:** `claude/AMBIENTE-CLAUDE-CODE.md`, `MANIFESTO.md`, `referencias/` (manual e estruturas) e as skills dentro de `.claude/skills/`. No repositório GitHub só há as skills genéricas (cartographer e automation-recommender). Parece que o projeto real está só na pasta do seu computador (`C:\Users\Multilaser\revisor-gdsxsr-projeto`), sem cópia no GitHub nem na nuvem. Não consegui abrir essa pasta daqui (precisa de autorização).
8. **A melhor automação possível é um verificador de citações em código** (script que extrai CPC/lei/súmula/tema/acórdão do DOCX e confere cada um nas fontes), descrito na seção 6.

## 2. Arquivos inúteis, duplicados ou pesados

Hoje o projeto tem na pasta de arquivos: `entregas/` 139 itens (6,5 MB), `votos-revisados/` 78 (5,5 MB), `uploads/` 85 (44 MB), `knowledge/` 33 (0,9 MB), `historico/` 39 (2 MB), `trabalho/` 70 (0,6 MB), `votos/` 8 e 3 PDFs na raiz (~207 MB).

| O que | Situação | Proposta (aguarda seu OK) |
|---|---|---|
| `... 2.docx` na raiz (4 arquivos: AGI 0741025-72, AGI 0743704-45, EMD 0707899-35, EMD 0711130-66) | Cópias **idênticas** (mesmo conteúdo, conferido por hash) dos arquivos sem o "2" | Remover os 4 "2" |
| `AGI 0739606-17 2.pdf` | Idêntico a `AGI 0739606-17.pdf` (45 MB cada) | Remover o "2" (-45 MB) |
| `0001746-54...processo.pdf` (116 MB) | Autos de um caso só, já com OCR em `trabalho/` | Tirar do projeto (guardar fora) se o caso estiver encerrado; o `.txt` do OCR basta |
| PDF `AGI 0739606-17` (45 MB) | O voto desse AGI já está em `votos/` | Idem: arquivar fora do projeto |
| `entregas/10 EMD 0708343-64 Sul-América...` | Idêntico ao de `entregas/rastreados/` | Manter só um |
| `historico/EMD 0705293-30 minuta anterior...` | Idêntico a `historico/originais-2026-10-07/9 EMD 0705293-30...` | Remover um |
| `historico/rodada-2026-10-08-conferencia/votos-revisados/` (1,4 MB) | Repete `votos-revisados/` (até no rastreado) | Remover a rodada antiga |
| `votos-revisados/` (78) vs `entregas/` (139) | Dois lugares para a mesma coisa (voto revisado), com nomes parecidos | Escolher **uma** pasta de entrega (`entregas/`, como as instruções dizem) e arquivar `votos-revisados/` em `historico/` |
| `uploads/hearth/` (85 arquivos com nome de código, 44 MB; 58 Word, 12 PDF, 7 zip, 6 "data") | Anexos das conversas, sem nome legível; 2 pares idênticos; os 2 maiores somam 27 MB | Abrir a lista, manter só o que ainda se usa, apagar o resto |
| `knowledge/claude/ferramentas/__pycache__/*.pyc` | Lixo gerado pelo Python | Remover |
| `knowledge/CALIBRACOES.md`, `...-v2.md`, `...-v3.md`, `claude/CALIBRACOES-...-v4.md` | Já consolidados em `CALIBRACOES-VIGENTES` (o próprio arquivo diz) | Mover para `historico/` (hoje ficam no caminho de busca e geram confusão) |
| `knowledge/historico/backup-*` e `historico/backup-*` | Versões v9–v15 completas das calibrações (~40–57 KB cada, 8 cópias) | Manter 1 ou 2 mais recentes; o resto vira lixo. O histórico de verdade está no Git (ver seção 5) |
| `votos/` | 8 minutas de trabalho de origens variadas | Mover as já concluídas para `entregas/` ou `historico/` |
| `description-full.md` e `UPGRADE-NOTES.md` | Texto da migração; já aparece nas instruções | Pode apagar depois de conferir |
| `docs/CODEBASE_MAP.md` | Gerado pelo plugin cartographer; não descreve nada deste projeto jurídico | Remover |

Estimativa de ganho: **cerca de 210 MB** só tirando PDFs repetidos e autos antigos; o resto é organização, não espaço.

## 3. Skills

**Úteis (manter), mas precisam de ajuste:**

| Skill | Tamanho | Problema | Ajuste |
|---|---|---|---|
| `revisar-voto-gdsxsr` | 22 KB | Desatualizada (concisão 7, v6, entrega rastreada, `project_read`, ferramentas inexistentes). Mistura regra de estilo (que já está nas calibrações) com procedimento | Reduzir para ~8 KB só de procedimento e apontar para as calibrações; corrigir os 4 conflitos |
| `coerencia-turma-gdsxsr` | 8 KB | Usa `buscar_hibrida` (não existe). Mantém "Precedentes 10 por dia" que já não vale | Reescrever com `pesquisar_decisoes` (modo `hibrida`, filtros `relator`, `orgao_julgador`, `data_julgamento_min`) |
| `pesquisar-jurisprudencia-gdsxsr` | 4 KB | Idem, nomes antigos; o "plano B" por WebFetch também falha (403/casca vazia) | Atualizar para as ferramentas atuais e deixar o plano B só como "pedir ao usuário" |
| `pesquisar-legislacao-gdsxsr` | 12 KB | Grande; já separa Planalto/SINJ/CNJ | Acrescentar `consultar_fonte_oficial` (operação `alteracoes` mostra se a lei foi alterada) e `pesquisar_normas` |
| `registrar-calibracao` | 7 KB | Depende de `project_read` e de `comparar_versoes.py` | Trocar leitura por caminho de arquivo |
| `atualizar-modelos-gdsxsr` | 5 KB | Só faz sentido se os modelos do Drive forem atualizados; usa `project_read` | Manter, mas só chamar quando Marcos pedir (não depois de toda calibração) |
| `ocr-pdf-gdsxsr` | 5 KB | Bom, medido | Manter. Registrar o aviso: o MarkItDown falha nos autos grandes |
| `minutar-voto-pje-gdsxsr` | 18 KB | Grande, só serve para minutar pelo PJe (Chrome) | Manter; carrega só quando for minutar |

**Skills de uso geral que aparecem na lista e não ajudam** (a lista de descrições entra em todo contexto): `pptx`, `xlsx`, `morning`, `deep-research`, `computer-use`, `built-in-browser`, `chrome-browser`, `google-workspace`, `import-memory`, `skill-creator`, `humanize-kit` (3), `omniout`, `dataviz`, `claude-api`, `cartographer` (3), `claude-automation-recommender` (2 cópias). Proposta: desligar, no ambiente do projeto, as que o gabinete não usa. Manter `docx`, `pdf` e, se usar o Drive, `google-workspace`. O `humanize-kit` não deve ser usado em voto: ele reescreve para "driblar detector", o que contradiz o objetivo do Gabinete (texto fiel e conferido).

## 4. Calibrações conflitantes, redundantes ou desatualizadas

Conflitos reais (a ordem de autoridade já manda prevalecer a calibração, mas **os arquivos antigos continuam lidos e confundem**):

1. **Concisão:** `C-02` v8 diz 8–8,5; a skill, o `agente.yaml` e `PERFIL-ESTILO-v1.1` dizem 7. O título de C-02 ainda diz "Concisão 7/10". Corrigir o título e os três arquivos.
2. **Entrega:** `C-44` (rastreado) × `C-47` (aceito, em cinza, só comentários). C-44 está parcialmente substituída; a skill (etapa 4) e `agente.yaml` (`tracked_changes: true`) ainda mandam entregar rastreado. Definir uma frase só: "edita rastreado para o portão, entrega aceito e guarda o rastreado".
3. **Item 3 da ementa:** `C-36` (numerar) substitui a orientação da skill e do perfil APC ("item 3 sem enumeração"). Os perfis ainda trazem o texto antigo.
4. **Linha de dados:** `C-3C` suprime a linha "Ação ajuizada em..." nos AGI; a skill descreve a linha para "APC; AGI e EMD adaptam". Dizer expressamente "só APC".
5. **Mini-dispositivo:** `C-3A` (curto, v8) × `C-3A` v16 (EMD acolhido, mais longo). A própria regra admite a tensão. Separar: não acolhimento = curto; acolhimento de EMD = com finalidade.
6. **Observações isoladas** (v12, v14, v16 "caso único") nunca foram reconfirmadas nem descartadas: C-27(d), C-3B, C-3F, C-39 v12, C-34 v14. Marcar data limite: se não reaparecerem em 3 minutas, descartar.
7. **Origem de `C-17`:** quase um artigo (v9, v10, v11 empilhadas, ~1.100 palavras). Dividir em C-17, C-17a (corte do bloco do assessor) e C-17b (precedente não lido).

Redundâncias:
- O **Registro de alterações** (tabela no fim, ~1.700 palavras) está fora de ordem (v15, v1.0, v8, v7, v6, v13, v14, v12...). Não precisa ser lido em toda revisão; mover para `historico/REGISTRO-CALIBRACOES.md`.
- "Origem: ..." de cada regra (nomes de processos, datas) ocupa quase metade do texto; é útil para auditoria, não para revisar. Mover para o registro.
- C-16 (conectores) e C-23 ("no mais", "no caso") tratam do mesmo vocabulário; juntar.
- C-02 (princípio) e C-11/12/13 (cadência) repetem limites; C-71 (portão) repete o que o `checar_voto.py` já testa.
- O resumo "Estilo" das instruções do projeto repete C-02, C-11, C-12, C-13 e C-20; basta apontar para as calibrações.

**Plano para o arquivo de calibrações:** manter um `CALIBRACOES-NUCLEO.md` de ~15 KB com só as regras ATIVAS em uma frase + um exemplo (todas as classes), e arquivos curtos por classe (`APC`, `AGI`, `EMD`) com o que só vale nelas. O revisor lê núcleo + a classe da minuta. A "origem" e o histórico vão para o registro. Isso reduz o custo fixo de cada revisão de ~17 mil para ~7–9 mil tokens, sem perder nenhuma regra.

## 5. Melhorias de estrutura (visão de programador, em português simples)

1. **Guardar tudo no Git.** O repositório GitHub quase vazio é o lugar certo: calibrações, perfis, skills, ferramentas (`checar_voto.py`, `revisao_tracked.py`...) e modelos. Cada calibração vira um commit, e os "backups" em pastas ficam desnecessários (o Git guarda todas as versões e mostra o que mudou). Sugestão de pastas: `regras/`, `perfis/`, `ferramentas/`, `skills/`, `modelos/`, `entregas/` (DOCX ficam fora do Git ou em pasta própria).
2. **Fonte única de regras:** hoje a mesma regra aparece nas instruções do projeto, na skill, no `agente.yaml`, no MANIFESTO e nas calibrações. Deixar **só as calibrações** como fonte, e os outros apontarem para elas. Cada duplicata é um lugar a mais para ficar desatualizado, como já aconteceu.
3. **Testes automáticos do `checar_voto.py`:** guardar 3–4 minutas "gabarito" (uma APC, um AGI, um EMD) e rodar o portão em todas após qualquer mudança em calibração ou ferramenta, para saber se algo quebrou.
4. **Regras novas viram teste.** Todo "C-xx" que for verificável por programa (recuo 4 cm, "ID" no singular, "– Grifei", EMENTA em negrito, admissibilidade sem negrito, realce de subtítulo, "e, no mérito," no dispositivo) vira checagem no `checar_voto.py`. A calibração v15 mostra que o agente errou as mesmas 5 coisas em muitas minutas (EMENTA sem negrito, realces faltando, último item sem nomear o recorrente, "e, no mérito,"): o programa pega isso de graça, sem gastar token de leitura.
5. **Modo "pré-voo":** antes de revisar, um script lista a classe, extrai ID/nomes/valores e já diz quais regras de formatação a minuta viola. O modelo só revisa o que o script não consegue (texto e direito).
6. **Rotina `Regenerar índice de modelos`** já existe; conferir se continua rodando e se o índice (223 KB, 1.220 linhas) é filtrado por script, nunca lido inteiro.
7. **Aproveitamento medido:** a calibração v15 mostra 98,8% das inserções mantidas por Marcos. O processo está maduro. O próximo ganho vem de menos tokens e de melhor conferência jurídica, não de mais regras de estilo.

## 6. Conferência de normas e precedentes: como evitar erro

Os erros mais prováveis, pelo que o próprio projeto já registrou: (a) base de dados atrasada (caso do Tema 1.230/STJ marcado "pendente" quando já estava julgado, C-60); (b) citar de memória ou de modelo antigo; (c) lei revogada (CC 786, C-64); (d) acórdão isolado tratado como tese; (e) tema com redação alterada; (f) dado do iajus/Precedentes sem o inteiro teor.

**Proposta em camadas (da mais barata para a mais forte):**

1. **Extrator automático de citações** (script Python em `ferramentas/`): lê o DOCX e lista, em uma tabela, tudo que parece citação: `CPC 373 I`, `CC 786`, `Súmula 362/STJ`, `Tema 1.085`, `REsp n. 1.863.973/SP`, `Acórdão n. ...`, `Lei 15.040/2024 94`. Dá a lista fechada do que precisa de conferência, para o revisor não depender de reler o voto.
2. **Conferência por tipo, sempre na ferramenta, sem memória:**
   - **Lei:** `consultar_fonte_oficial` (operação `alteracoes` mostra se a norma foi alterada ou revogada) + `ler_documento` para o texto + Planalto/SINJ como fonte final. O comentário C-63 recebe o texto **copiado da ferramenta**, nunca digitado.
   - **Súmula, tema, IRDR, IAC:** `pesquisar_precedentes` por número, com `tribunal` e `tipo`; o campo de situação (cancelada/superada) entra no comentário. Se o iajus disser "pendente" ou "sem tese", confirmar no site do STJ/STF (regra C-60 já existente; torná-la obrigatória no checklist).
   - **Acórdão:** `pesquisar_decisoes` modo `cnj` ou `textual` com frase exata; conferir número, relator, órgão, data **e trecho citado** contra o texto.
3. **Regra de bloqueio:** citação sem registro devolvido pela ferramenta não entra no voto; vai ao comentário "não localizado" (já previsto em C-24/C-52), nunca fica "mais ou menos certa".
4. **Dupla fonte para o que decide o resultado:** tema, súmula ou acórdão que sustenta o dispositivo exige duas fontes (ferramenta + site oficial), as demais uma.
5. **Cache de conferências:** guardar em `regras/CONFERIDOS.csv` o que já foi conferido (norma/tema, data da conferência, fonte, situação, redação). Reaproveitar por 30 dias (temas e súmulas mudam pouco; leis alteradas mudam mais), economizando consultas e tokens. Tema "pendente" nunca fica no cache.
6. **Aviso de vigência por data do fato:** extrair as datas do caso e comparar com a data de vigência devolvida (caso do CC 786/Lei 15.040/2024).
7. **Segundo olhar barato:** ao fim, um subagente de "advogado do diabo" (modelo menor) recebe só a lista de citações e as respostas das ferramentas e aponta o que não bate. Não lê o voto inteiro.
8. **Relatório de conferência** (1 linha por citação: ok / ajustada / não localizada + fonte) anexado à entrega, para você ver rápido onde olhar.

**Limite que vale registrar:** a ferramenta `verificar_citacoes`, citada nas instruções do conector Precedentes e na skill, **não apareceu** na lista de ferramentas disponíveis desta sessão (só as de peças/licitação). Se for uma ferramenta que você contratou, vale reconectar o servidor; se não existir mais, tirá-la da skill.

## 7. Tokens: onde está o gasto e como cortar

| Gasto fixo por revisão | Hoje | Depois |
|---|---|---|
| Calibrações | ~17 mil tokens | ~7–9 mil (núcleo + classe) |
| Skill `revisar-voto` | ~5,5 mil | ~2 mil |
| Perfil de classe | 3–4 mil | 3–4 mil (manter) |
| Lista de skills/plugins no contexto | dezenas de descrições irrelevantes a cada turno | só as do projeto |
| Índice de modelos | 223 KB; só é barato se filtrado por script | idem; garantir `pandas` sempre |
| PDFs de autos | pode custar centenas de mil tokens | `pdftotext` + `grep`, como a skill já manda |

Outras economias: (1) rodar o portão e o extrator de citações antes de qualquer leitura completa; (2) ler só o VOTO dos modelos, nunca o relatório copiado (já previsto); (3) 3 modelos, não 8, salvo matéria nova; (4) em lote, carregar regras uma vez e processar as minutas em sequência (já previsto); (5) usar subagentes menores para tarefas mecânicas (extração, conferência bruta) e deixar o modelo principal para o texto; (6) comentários mecânicos agrupados em um só (C-55, já existe).

## 8. Ferramentas, plugins, MCP e API úteis

**Manter / usar mais:** `docx` e `pdf` (skills), `iajus` (nomes novos), Google Drive (modelos), `ocr_pdf.py`, MarkItDown para PDFs com texto.

**Desligar no projeto:** `claude-mem` (memória própria que duplica a memória do projeto e grava dados de processos judiciais em outro lugar; é também risco de sigilo), `headroom`, `cartographer`, `claude-code-setup`. A única utilidade de `claude-code-setup` já foi usada neste diagnóstico.

**Considerar:**
- **Hooks do Claude Code** (automação sem gastar token): ao salvar um DOCX em `entregas/`, rodar `checar_voto.py` e o extrator de citações; bloquear a entrega se houver ERRO.
- **Skill `conferir-citacoes-gdsxsr`** nova, só com o procedimento da seção 6.
- **Skill única de entrega** que une `revisar-voto` + `coerencia-turma`, rodando em sequência (hoje são duas leituras de contexto).
- **MCP do iajus**: já conectado; usar `pesquisar_decisoes` com `relator="Sérgio Rocha"` e `orgao_julgador` para a coerência da Turma; `consultar_acervo` informa a cobertura do acervo (útil para saber quando "zero resultado" não é prova de ausência).
- **API da Anthropic (opcional, futuro):** para lote grande, a Batch API reduz o custo; cache de prompt reduz o custo das calibrações fixas. Só vale se for rodar fora do Claude Code (programa próprio). Hoje não é necessário.
- **Conferência de legibilidade:** nada de ferramentas "anti-detector" de IA (o `humanize-kit`): o critério do projeto é voto fluido, fiel e conferido, não passar em detector.

## 9. Ordem sugerida de execução

| # | Ação | Risco | Ganho |
|---|---|---|---|
| 1 | Autorizar acesso à pasta `C:\Users\Multilaser\revisor-gdsxsr-projeto` para comparar com a nuvem e subir tudo ao GitHub | baixo | alto (fonte única) |
| 2 | Corrigir os 4 conflitos (concisão, entrega, item 3, linha de dados) em skill, yaml e perfis | baixo | alto |
| 3 | Atualizar as 3 skills de pesquisa para as ferramentas atuais (iajus) | baixo | alto |
| 4 | Remover duplicatas exatas e PDFs repetidos (lista da seção 2) | baixo | médio (-210 MB) |
| 5 | Dividir calibrações em núcleo + classe + registro | médio (precisa conferir que nenhuma regra se perde) | alto (tokens) |
| 6 | Escrever o extrator de citações e o `CONFERIDOS.csv` | médio | alto (qualidade) |
| 7 | Desligar plugins/skills não usadas | baixo | médio |
| 8 | Hooks e testes-gabarito | médio | médio |

Digo qual desses começo quando você aprovar. Recomendo 2, 3 e 4 primeiro.
