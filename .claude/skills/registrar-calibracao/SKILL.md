---
name: "registrar-calibracao"
description: "Compara a revisão do agente com a versão final do Des. Sérgio Rocha ou de Marcos, extrai regras gerais e atualiza as calibrações GDSXSR. Usar quando o usuário enviar a versão final de um voto."
---

# Registrar calibração GDSXSR

Fecha o ciclo de aprendizado do Assessor GDSXSR: **versão do agente → versão final (Desembargador ou Marcos) → comparação → regra geral → arquivos de calibração**. O objetivo é aprender **regras**, não memorizar textos.

## Onde ficam as regras (v17, 13/10/2026)

- `claude/CALIBRACOES-NUCLEO-GDSXSR.md`: regras de todas as classes.
- `claude/CALIBRACOES-APC-GDSXSR.md`, `CALIBRACOES-AGI-GDSXSR.md`, `CALIBRACOES-EMD-GDSXSR.md`: regras de uma só classe.
- `claude/CALIBRACOES-VIGENTES-GDSXSR.md`: apenas índice.
- `historico/REGISTRO-ALTERACOES-CALIBRACOES.md`: tabela de versões e "Origem" de cada regra.

## Entradas

- **Versão final** (obrigatória): DOCX liberado ou ajustado. Identifique quem corrigiu (Desembargador, Marcos, assessor), pelo usuário ou pelo nome do arquivo ("corrigido", "alterado", "ajustado", "Marcos").
- **Versão do agente**: o DOCX entregue pela skill `revisar-voto-gdsxsr` (a rastreada fica em `entregas/rastreados/`). Procure-o nesta ordem: anexo do usuário → pasta do projeto (mesmo nome sem a alteração final) → Drive. Se não existir, compare com a **minuta original do assessor** e diga que a calibração mede a diferença entre a minuta e a versão final, não o desempenho do agente.
- Se o usuário só descrever a correção em texto, registre-a do mesmo modo, sem o script.

## Etapa 1 — Carregar o estado atual

Leia o núcleo e o arquivo da classe da minuta. Anote a versão atual (ex.: v17) e o último código C-xx de cada grupo. Sem acesso aos arquivos, pare e peça-os, porque registrar sem eles gera duplicatas e conflitos.

## Etapa 2 — Comparar

Use `claude/ferramentas/comparar_versoes.py` e `claude/ferramentas/revisao_tracked.py` do projeto (fonte única dos scripts; não os reescreva de memória), copiados para a pasta de trabalho, e rode:
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

Para cada regra nova ou alterada, use o formato dos arquivos vigentes:

```markdown
**C-xx · Título curto** — ATIVA · classes · vN
Regra em uma a três frases, como instrução. Exemplo antes → depois (trecho curto, sem dados pessoais desnecessários).
```

- Regra de todas as classes vai no núcleo; regra de uma só classe, no arquivo da classe. A "Origem" (processo nº, quem corrigiu, data) vai para o registro, não para as regras.
- Numere no grupo certo (A princípios, B cadência, C referências e voz, D estrutura, E formatação, F comentários, G jurisprudência, H arquivo e entrega), seguindo o último código do grupo.
- Se a regra refina uma existente, **edite a regra existente**, em vez de duplicá-la.
- Se substitui, marque a antiga `SUBSTITUÍDA por C-yy · vN` e mova o texto antigo para o registro.
- Se vale só para uma matéria (PASEP, família, execução), marque `ESPECÍFICA`. Quando a regra for de **resultado por matéria**, proponha a atualização do perfil decisório correspondente, e não dos arquivos de calibração.
- Não invente motivo: se o porquê da correção não estiver claro, registre a regra como observada e diga isso.

## Etapa 5 — Gravar e propagar

1. **Backup antes de gravar:** copie os arquivos que serão alterados para `historico/backup-AAAA-MM-DD/`.
2. Suba a versão (v17 → v18), atualize a linha de versão e data no topo do núcleo e acrescente uma linha à tabela do registro.
3. Grave os arquivos inteiros, com o conteúdo completo atualizado. Antes de gravar, confira que nenhuma regra existente foi perdida.
4. Se a regra exigir mudança no portão automático (`checar_voto.py`) ou na skill `revisar-voto-gdsxsr` (estrutura, fórmulas, formatação), diga isso no fim e ofereça propor a atualização da skill. Não altere a skill sem o usuário pedir.
5. Se a versão final for de alta qualidade, sugira promovê-la a MODELO OURO no Drive (`01 — MODELOS OURO/<classe>`). Não mova arquivos sem autorização.

## Etapa 6 — Relatório ao usuário

Curto, no chat (uma linha por item, sem transcrever as regras inteiras, que já estão nos arquivos):
- comparação feita (arquivos, quem corrigiu) e total de diferenças;
- taxa de aproveitamento das alterações do revisor (mantidas × rejeitadas/desfeitas) e as rejeições mais relevantes;
- regras **novas**, **alteradas** e **substituídas**, com códigos e uma linha cada;
- diferenças descartadas e por quê (fato do caso, preferência isolada);
- métricas antes × depois quando revelarem tendência (ex.: mediana do voto 52 → 31 palavras);
- dúvidas que dependem de confirmação e mudanças sugeridas na skill de revisão.