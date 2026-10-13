---
name: "atualizar-modelos-gdsxsr"
description: Depois de cada calibração GDSXSR registrada (ou quando o usuário pedir), verifica quais regras novas ou alteradas devem refletir nos modelos e estruturas prontas do Gabinete do Des. Sérgio Rocha/TJDFT no Drive e devolve, para cada modelo afetado, um DOCX de proposta com as mudanças aplicadas em cinza e comentário explicando cada uma, sem gravar nada no Drive. Usar logo após registrar-calibracao e sempre que o usuário falar em atualizar, ajustar ou revisar modelos, estruturas prontas, manual ou modelos ouro, mesmo sem dizer o nome da habilidade.
---

# Atualizador de modelos — GDSXSR

O Revisor aprende com cada calibração, mas os modelos de partida no Drive continuam com a forma antiga. Com o tempo, o assessor começa a minuta de um modelo desatualizado e o Revisor corrige sempre as mesmas coisas. Esta habilidade fecha esse ciclo: traduz as regras de calibração em **propostas** de mudança nos modelos, para que Marcos decida e aplique. Ela **nunca grava nem move nada no Drive**.

## Quando roda

- **Após cada calibração:** ao fim de `registrar-calibracao`, rode esta habilidade sobre as regras novas, alteradas ou substituídas naquela versão.
- **Sob pedido:** quando Marcos pedir para revisar os modelos. Sem indicação de versão, considere todas as regras ATIVAS e compare com os modelos atuais.

## Etapa 1 — Separar as regras que tocam os modelos

Use `claude/CALIBRACOES-NUCLEO-GDSXSR.md` e os arquivos de classe; se ele já foi lido nesta conversa (por exemplo, por `registrar-calibracao`), não leia de novo. Após uma calibração, use o **Registro de alterações** (`historico/REGISTRO-ALTERACOES-CALIBRACOES.md`) para pegar só as regras da versão nova (novas, alteradas, substituídas).

Uma regra toca os modelos quando muda algo que já aparece pronto no modelo antes de o assessor escrever o caso:

| Toca os modelos | Não toca |
|---|---|
| Estrutura e ordem das seções, títulos, fórmulas fixas (abertura, conhecimento, dispositivo, honorários recursais), formatação (fonte, recuo, alinhamento, negrito, realce), modo de citar ementas e dispositivos, nomenclatura do arquivo | Correções de fato de um caso, escolha de palavra isolada, linha decisória por matéria (vai para o perfil decisório), cadência do texto de mérito que o assessor redige caso a caso |

Regra ESPECÍFICA (PASEP, família, execução) só toca os modelos daquela matéria.

Se nenhuma regra tocar os modelos, diga em uma linha: "Calibração vN: nenhuma regra muda os modelos." e pare.

## Etapa 2 — Achar os modelos afetados

Fontes, nesta ordem:

1. **Estruturas prontas e Manual** (pasta do Drive id `1aEgy58IgkjNOvu0zAYhREeOXViIZeUHI`): `MANUAL ATUALIZADO` e as estruturas por classe (`X APC 0000000-00 …`, `X AGI …`, `X EMD …`). São o alvo principal: é delas que toda minuta parte.
2. **Modelos por matéria** pelo índice `claude/INDICE-MODELOS-GDSXSR.csv` (filtre com pandas por Classe, Matéria e Temas da regra). Use só os de Nível 1 (OURO) e 2.

Os **MODELOS OURO são votos reais já julgados**: não proponha reescrever o texto deles. Quando um modelo ouro contrariar uma regra vigente, não gere DOCX; liste-o no relatório como "modelo ouro com forma superada pela C-xx", sugerindo marcá-lo ou substituí-lo por um voto mais recente. Proposta em DOCX é para estrutura pronta, Manual e modelos que funcionam como formulário.

Para cada candidato, baixe o DOCX (`download_file_content`), salve o texto na pasta de trabalho e confira com `grep` ou `python-docx`, sem despejar o modelo inteiro no contexto, se a regra **já está atendida**. Modelo que já segue a regra fica fora; não gere proposta vazia.

## Etapa 3 — Montar a proposta

Para cada modelo afetado, gere uma cópia com as mudanças propostas, no mesmo padrão visual do Revisor (preferência de Marcos):

- alteração já aplicada, texto novo em **cinza**, sem exigir aceitar/rejeitar uma a uma;
- **comentário lateral** em cada alteração, autor `Revisor GDSXSR – Modelos`, no formato: `C-xx (vN): [regra em uma linha]. Antes: "…" → agora: "…".`
- mude só o que a regra exige; não aproveite para "melhorar" outras partes do modelo, porque Marcos precisa conseguir conferir cada mudança contra uma regra.

Use a ferramenta da revisão, `claude/ferramentas/revisao_tracked.py` (lida do projeto; não a reescreva de memória). Sem ela, avise o usuário e use a habilidade `docx`.

Nome do arquivo: `PROPOSTA – <nome original sem extensão> – calibração vN.docx`.

Ao final, converta cada DOCX para PDF (`soffice --headless --convert-to pdf`) e olhe as páginas alteradas em folha de contato (`pdftoppm -r 60` + `montage`) para confirmar que a formatação do modelo não quebrou.

## Etapa 4 — Entregar e relatar

Envie os DOCX na conversa (não grave em pasta nem no Drive). Relatório curto no chat:

- regras da calibração que tocam modelos (código e uma linha cada);
- modelos com proposta, e quantas alterações em cada;
- modelos já conformes (só a contagem);
- modelos ouro com forma superada, se houver;
- regras que pedem mudança no **Manual** ou nas skills (`revisar-voto-gdsxsr`, `minutar-voto-pje-gdsxsr`), para Marcos decidir.

Termine lembrando, em uma frase, que nada foi alterado no Drive e que, aprovada a proposta, basta substituir o modelo na pasta.
