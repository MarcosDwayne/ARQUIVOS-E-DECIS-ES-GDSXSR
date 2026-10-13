---
name: "coerencia-turma-gdsxsr"
description: "Confere se a minuta de voto (APC, AGI, EMD) do Gabinete do Des. Sérgio Rocha/TJDFT está alinhada com o que o próprio Desembargador e a 4ª Turma Cível decidiram no último ano e, só quando houver divergência ou Turma dividida, insere comentário lateral no DOCX com os julgados. Usar sempre junto com a revisão de minuta (revisar-voto-gdsxsr) e também quando o usuário pedir para checar coerência, entendimento da Turma, como o Desembargador costuma decidir, ou se a minuta \"vai contra\" a Turma, mesmo sem dizer o nome da habilidade."
---

# Coerência com a Turma — GDSXSR

Esta etapa protege o voto de um risco que a revisão de estilo não enxerga: a minuta pode estar bem escrita e, ainda assim, decidir de forma diferente do que o Des. Sérgio Rocha ou a 4ª Turma Cível vêm decidindo. Divergência não é erro em si (pode haver distinção legítima), mas o Desembargador precisa saber dela antes de levar o voto à sessão. Por isso a habilidade **não altera texto nem resultado**: ela só avisa, em comentário lateral, com os julgados que sustentam o alerta.

## Quando roda

- **Dentro da revisão:** depois que `revisar-voto-gdsxsr` termina o texto e antes da entrega, aplique esta etapa ao mesmo DOCX. Os comentários entram no mesmo arquivo revisado.
- **Avulsa:** quando o usuário enviar uma minuta (revisada ou não) e pedir a checagem. Nesse caso o DOCX de saída é uma cópia da minuta só com os comentários de coerência, sem qualquer alteração no texto.

## Economia de tokens

A pesquisa e a classificação ficam inteiras; corta-se o retrabalho. Dentro da revisão, use a minuta e as ferramentas já carregadas, sem reler nem baixar de novo. Das buscas, guarde só os julgados pertinentes a cada questão e descarte o resto sem comentá-lo. Ao abrir um link com WebFetch, peça no `prompt` apenas a solução dada à questão e o resultado, não o resumo do acórdão.

## Parâmetros fixos (escolhas do usuário)

- **Fontes:** votos do Des. Sérgio Rocha como relator e acórdãos da 4ª Turma Cível do TJDFT. Não compare com outras Turmas nem use STJ/STF para esta etapa (isso já é feito pela revisão).
- **Período:** últimos 12 meses contados da data de hoje.
- **Saída:** comentário lateral no DOCX, **apenas** quando houver divergência ou Turma dividida. Minuta alinhada não recebe comentário.

## Etapa 1 — Extrair as questões decididas

Leia a minuta e liste as questões jurídicas que de fato decidem o recurso, cada uma com a solução que a minuta dá. Exemplo:

| # | Questão | Solução na minuta | Onde está (início do parágrafo) |
|---|---|---|---|
| 1 | Negativação sem prova da contratação gera dano moral in re ipsa? | Sim | "No caso, a ré não comprovou..." |
| 2 | Valor da indenização por negativação indevida | Mantém R$ 5.000,00 | "Quanto ao valor..." |

Foque no que muda o resultado: mérito, preliminares acolhidas ou rejeitadas, valores de indenização, termo inicial de juros e correção, distribuição de sucumbência quando discutida. Deixe de fora o que é rotina e não varia entre julgadores (conhecimento do recurso preenchido, honorários recursais do art. 85, § 11, do CPC aplicados de modo padrão). Em geral sobram de 1 a 5 questões; se passar de 6, fique com as 6 que mais pesam no resultado.

## Etapa 2 — Pesquisar

Use o conector **IAJUS**, ferramenta `mcp__mcp_iajus_com_br__pesquisar_decisoes` (carregue com ToolSearch), com `busca.modo="hibrida"`. Para cada questão, faça duas buscas:

1. Votos do Desembargador:
   `filtros.tribunal="TJDFT"`, `filtros.relator="Sérgio Rocha"`, `filtros.data_julgamento_min=<hoje − 12 meses, AAAA-MM-DD>`, `limite=10`
2. Turma:
   `filtros.tribunal="TJDFT"`, `filtros.orgao_julgador="4ª Turma Cível"`, `filtros.data_julgamento_min=<mesma data>`, `limite=15`

Escreva a `consulta` como a questão jurídica em linguagem natural, com os fatos relevantes e **sem nomes de partes, CPF ou número do processo da minuta** (o conector proíbe dados pessoais e eles não melhoram a busca). Ex.: "inscrição em cadastro de inadimplentes sem prova da contratação dano moral valor da indenização".

Leia a ementa devolvida. Quando ela não mostrar a solução da questão, use `ler_documento` ou abra o link oficial devolvido (JurisDF) com WebFetch e procure o trecho. Descarte resultados que tratem de outra questão: a busca por sentido traz vizinhos que não servem.

Se o IAJUS falhar, diga isso no relatório e não conclua por ausência de julgados: a ferramenta avisa que zero resultado não certifica cobertura.

Se a busca avisar que a lista pode estar incompleta, não conclua por ausência: varie a redação da consulta uma vez antes de decidir.

## Etapa 3 — Classificar cada questão

Para cada questão, compare a solução da minuta com os julgados pertinentes encontrados:

- **Alinhada:** os julgados pertinentes decidem como a minuta. → nada a comentar.
- **Diverge do Desembargador:** há voto(s) do Des. Sérgio Rocha no período decidindo de forma diferente. → comentar. Este é o alerta mais importante, porque o voto sai em nome dele.
- **Diverge da Turma:** os votos do Desembargador estão alinhados ou ausentes, mas a maioria dos acórdãos da 4ª Turma Cível decide de outro modo. → comentar.
- **Turma dividida:** relatores da Turma decidem a questão de formas diferentes no período. → comentar, indicando o lado de cada relator e onde está o Desembargador, se houver voto dele.
- **Sem julgados pertinentes no período:** → não comentar no DOCX; registre no relatório final em uma linha.

Diferença só de valor (indenização, honorários) conta como divergência quando sair claramente da faixa praticada pela Turma para casos semelhantes; diferença pequena, explicada pelas peculiaridades do caso, não conta.

Antes de marcar divergência, verifique se os julgados contrários não têm fato distintivo evidente (ex.: houve prova da contratação lá e não aqui). Se tiverem, a questão é alinhada.

## Etapa 4 — Comentar no DOCX

Ancore o comentário no início do parágrafo em que a minuta resolve a questão. Autor do comentário: `Assessor GDSXSR – Coerência`. Use a mesma ferramenta de comentários da revisão (`claude/ferramentas/revisao_tracked.py`, lida do projeto; não a reescreva de memória). Sem ela, use a habilidade `docx` só para inserir comentários, sem tocar no texto.

Formato do comentário (curto, direto, sem opções para o usuário escolher):

```
COERÊNCIA (últimos 12 meses) — [Diverge do Desembargador | Diverge da Turma | Turma dividida]
A minuta conclui [solução em uma linha]. [Quem] decidiu de modo diverso: [solução contrária em uma linha].
• Proc. 0000000-00.0000.8.07.0000, Rel. Des. [nome], julgado em DD/MM/AAAA — [resultado em poucas palavras]. [link]
• (até 3 julgados, priorizando os do Des. Sérgio Rocha e os mais recentes)
Contagem na pesquisa: X de Y julgados pertinentes encontrados no sentido contrário.
Para manter a solução, convém explicitar no voto o fato que distingue este caso.
```

Regras do comentário:
- Cite só processo, relator, data e resultado que vieram da busca; nunca complete de memória.
- Copie o link exatamente como veio.
- A contagem é do que a pesquisa encontrou, não do universo de julgados; escreva "na pesquisa".
- Não mude o texto nem o resultado da minuta. Decidir se diverge ou não é do Desembargador e de Marcos.

## Etapa 5 — Relatório

Se estiver dentro da revisão, acrescente ao relatório da revisão um bloco de no máximo 4 linhas. Se for avulsa, este é o relatório inteiro:

- questões examinadas (número) e quantas geraram comentário;
- para cada comentário, uma linha: questão → tipo de divergência;
- questões sem julgados no período;
- se o IAJUS falhou ou se a lista veio marcada como possivelmente incompleta.

Entregue o DOCX na conversa (não grave em pasta), com o mesmo nome da minuta revisada; na versão avulsa, acrescente " – coerência" antes da extensão.