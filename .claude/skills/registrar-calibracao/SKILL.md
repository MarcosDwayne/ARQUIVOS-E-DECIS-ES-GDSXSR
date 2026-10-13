---
name: "registrar-calibracao"
description: "Compara a revisão do agente com a versão final do Des. Sérgio Rocha ou de Marcos, extrai regras gerais e atualiza as calibrações GDSXSR. Usar quando o usuário enviar a versão final de um voto."
---

# Registrar calibração GDSXSR

Fecha o ciclo de aprendizado do Revisor de Votos: **versão do agente → versão final (Desembargador ou Marcos) → comparação → regra geral → os arquivos de calibração (núcleo para regra geral; arquivo da classe para regra de uma classe; "Origem" e a linha da versão em `historico/REGISTRO-ALTERACOES-CALIBRACOES.md`). Antes de gravar, faça backup em `historico/backup-AAAA-MM-DD/`**. O objetivo é aprender **regras**, não memorizar textos.

## Entradas

- **Versão final** (obrigatória): DOCX liberado ou ajustado. Identifique quem corrigiu (Desembargador, Marcos, assessor), pelo usuário ou pelo nome do arquivo ("corrigido", "alterado", "ajustado", "Marcos").
- **Versão do agente**: o DOCX entregue pela skill `revisar-voto-gdsxsr`. Procure-o nesta ordem: anexo do usuário → pasta conectada (mesmo nome sem a alteração final) → Drive. Se não existir, compare com a **minuta original do assessor** e diga que a calibração mede a diferença entre a minuta e a versão final, não o desempenho do agente.
- Se o usuário só descrever a correção em texto, registre-a do mesmo modo, sem o script.

## Etapa 1 — Carregar o estado atual

Leia `claude/CALIBRACOES-NUCLEO-GDSXSR.md` e o arquivo da classe da minuta (`CALIBRACOES-APC/AGI/EMD-GDSXSR.md`) no projeto; o registro de versões está em `historico/REGISTRO-ALTERACOES-CALIBRACOES.md`. Anote a versão atual (ex.: v5) e o último código C-xx de cada grupo. Sem acesso ao projeto, pare e peça o arquivo, porque registrar sem ele gera duplicatas e conflitos.

## Etapa 2 — Comparar

Copie para a mesma pasta de trabalho `claude/ferramentas/comparar_versoes.py` e `claude/ferramentas/revisao_tracked.py` (fonte única dos scripts; não os reescreva de memória) e rode:
`python3 comparar_versoes.py AGENTE.docx FINAL.docx > diff.txt`

Leia o `diff.txt` por partes (`grep -n`, `sed -n`), começando pelo destino das alterações rastreadas e pelas mudanças de formatação; não o despeje inteiro no contexto quando passar de algumas centenas de linhas.

A versão do agente vem com controle de alterações (C-44). O comparador usa a versão aceita de cada arquivo e informa, ao final, o **destino de cada alteração rastreada do agente**: inserções mantidas × rejeitadas e exclusões mantidas × desfeitas, julgadas pelo contexto da frase. Inserção rejeitada e exclusão desfeita são os sinais mais fortes de calibração: mostram o que o revisor mudou e o Desembargador ou Marcos não quiseram. Se a versão final ainda tiver alterações pendentes, o relatório avisa.

O relatório traz também, por seção: parágrafos ALTERADOS (diff por palavra), SUPRIMIDOS, ACRESCENTADOS, CISÕES e FUSÕES, mudanças de FORMATAÇÃO (alinhamento, negrito, tamanho, realce), métricas do voto (mediana de palavras, parágrafos com 2+ períodos e com <15 palavras) e comentários removidos ou novos. Abra os trechos completos nos dois arquivos só quando o diff for ambíguo, e só os parágrafos em questão. Se houver página relevante (RELATÓRIO no topo, quebras), renderize os dois com `soffice --headless --convert-to pdf` e compare só as páginas em questão.

## Etapa 3 — Classificar cada diferença

Para cada item do diff, decida:

| Tipo | Exemplo | Vira regra? |
|---|---|---|
| **Estilo/estrutura generalizável** | cisão de período conclusivo; "no mais" por "ademais"; título à esquerda | Sim |
| **Formatação** | alinhamento, negrito, fonte, espaçamento | Sim, se repetível |
| **Conteúdo jurídico** | tese aplicada, distinção, resultado alterado | Só como linha decisória (perfil decisório ou comentário C-53), nunca como regra de estilo |
| **Fato do caso** | ID, nome, valor, data corrigidos | Não. No máximo regra de método ("conferir nome do juiz no PJe") |
| **Limpeza de trabalho** | comentários de pendência apagados | Normalmente não (C-52 já cobre) |
| **Preferência isolada** | troca de palavra única, sem padrão | Não; registre como observação se reaparecer |

Uma diferença vira regra quando: (a) o motivo é inferível e vale fora deste caso; (b) não contradiz regra vigente, ou a contradição é intencional, e então a antiga fica SUBSTITUÍDA; (c) pode ser descrita como instrução verificável ("faça X quando Y"). Em dúvida, pergunte ao usuário antes de gravar, em uma só pergunta objetiva com as hipóteses.

## Etapa 4 — Redigir as regras

Para cada regra nova ou alterada, use o formato do arquivo vigente:

```markdown
**C-xx · Título curto** — ATIVA · classes · vN
Regra em uma a três frases, como instrução. Exemplo antes → depois (trecho curto, sem dados pessoais desnecessários). Origem: processo nº, quem corrigiu, data.
```

- Numere no grupo certo (A princípios, B cadência, C referências e voz, D estrutura, E formatação, F comentários, G jurisprudência, H arquivo e entrega), seguindo o último código do grupo.
- Se a regra refina uma existente, **edite a regra existente** e acrescente a origem, em vez de duplicá-la.
- Se substitui, marque a antiga `SUBSTITUÍDA por C-yy · vN` e mantenha o texto como histórico.
- Se vale só para uma matéria (PASEP, família, execução), marque `ESPECÍFICA`. Quando a regra for de **resultado por matéria**, proponha a atualização do perfil decisório correspondente, e não deste arquivo.
- Não invente motivo: se o porquê da correção não estiver claro, registre a regra como observada e diga isso.

## Etapa 5 — Gravar e propagar

1. Suba a versão (v5 → v6; v6 → v7), atualize a linha de versão e data no topo e acrescente uma linha ao **Registro de alterações**.
2. Grave o arquivo inteiro com `project_write` em `claude/CALIBRACOES-VIGENTES-GDSXSR.md`, com o conteúdo completo atualizado. Antes de gravar, confira que nenhuma regra existente foi perdida.
3. Se a regra exigir mudança no portão automático (`checar_voto.py`) ou na skill `revisar-voto-gdsxsr` (estrutura, fórmulas, formatação), diga isso no fim e ofereça propor a atualização da skill. Não altere a skill sem o usuário pedir.
4. Se a versão final for de alta qualidade, sugira promovê-la a MODELO OURO no Drive (`01 — MODELOS OURO/<classe>`). Não mova arquivos sem autorização.

## Etapa 6 — Relatório ao usuário

Curto, no chat (uma linha por item, sem transcrever as regras inteiras, que já estão no arquivo):
- comparação feita (arquivos, quem corrigiu) e total de diferenças;
- taxa de aproveitamento das alterações do revisor (mantidas × rejeitadas/desfeitas) e as rejeições mais relevantes;
- regras **novas**, **alteradas** e **substituídas**, com códigos e uma linha cada;
- diferenças descartadas e por quê (fato do caso, preferência isolada);
- métricas antes × depois quando revelarem tendência (ex.: mediana do voto 52 → 31 palavras);
- dúvidas que dependem de confirmação e mudanças sugeridas na skill de revisão.