---
name: "pesquisar-jurisprudencia-gdsxsr"
description: "Plano B de jurisprudência (TJDFT, STJ, STF) do Assessor GDSXSR: usar SOMENTE quando a ferramenta iajus falhar, não abrir ou não localizar o precedente."
---

# Jurisprudência: plano B quando o iajus falhar (GDSXSR)

## Quando usar
O caminho principal é sempre a ferramenta iajus (`pesquisar_decisoes` com `busca.modo` `hibrida`, `textual` ou `cnj`; `pesquisar_precedentes` para súmula e tema por número; `ler_documento` para o texto integral; carregar com ToolSearch se estiver diferida). Esta skill só entra se o iajus:
- der erro, ficar fora do ar ou não estiver conectado;
- devolver resultado vazio ou sem o precedente procurado, mesmo após refinar a consulta uma vez (zero não certifica cobertura);
- não trouxer ementa, tese ou dado essencial (relator, órgão, data).
Nesses casos, registrar em uma linha por que o iajus não bastou e seguir abaixo. Se o iajus funcionou, não fazer pesquisa paralela nos sites.

## Escalonamento obrigatório (C-72)
Se o plano B abaixo também não conferir o precedente, não pare: (1) busque na web (Google ou Bing) até o texto na fonte oficial ou em fonte confiável que reproduza o acórdão; (2) abra o portal oficial (JurisDF, SCON/STJ, STF) pela extensão Claude no Chrome (skill `chrome-browser`), se as ferramentas do navegador estiverem na thread. Só depois de esgotar esses caminhos o precedente fica pendente, com uma linha sobre o que foi tentado e o que falhou e comentário lateral (C-52). O voto nunca sai com precedente não conferido apresentado como conferido.

## Regra-mãe
Só afirmar o que a fonte devolveu nesta conversa. Número, relator, órgão, data, tese e vigência vêm do site oficial, nunca de memória. O Dizer o Direito serve só para descobrir; nunca é fundamento. Não colocar nomes de partes ou dados pessoais em buscas. O registro do iajus pode estar defasado (C-60): tema "pendente" ou "sem tese" não se afirma no voto sem conferir o andamento no site do STJ/STF.

## Dois usos
1. Conferir precedente já citado na minuta: localizar pelo número, ler ementa/tese e confirmar se diz o que a minuta afirma.
2. Descobrir precedente novo sobre uma tese.

## Ordem das fontes (obrigatória)
1. TJDFT, 4ª Turma Cível e Des. Sérgio Rocha.
2. TJDFT como um todo (IRDR, IAC, Jurisprudência em Temas, informativos).
3. STJ (súmulas, repetitivos, pesquisa pronta, acórdãos).
4. STF (súmulas vinculantes e não vinculantes, repercussão geral, acórdãos).

## Sites oficiais (WebFetch), situação testada em 07/10/2026
- Abriram: scon.stj.jus.br/SCON/sumstj/toc.jsp (súmulas STJ); scon.stj.jus.br/SCON/repetitivos/listaRR.jsp (repetitivos); tjdft.jus.br/consultas/jurisprudencia/jurisprudencia-em-temas.
- Abre só a casca, sem conteúdo (roda no navegador): jurisdf.tjdft.jus.br. Não tirar conclusão dele pelo WebFetch.
- Erro 403: portal.stf.jus.br (repercussão geral e inteiro teor).
- Não confirmados: scon.stj.jus.br/SCON/ (raiz), /jt/jt.jsp, /pesquisa_pronta/listaPP.jsp, informativos do TJDFT, jurisprudencia.stf.jus.br (súmulas). Tentar uma vez cada; se falhar, seguir adiante.
- curl direto falhou em todos (rede do ambiente); não insistir.
- Outras ferramentas: o conector Precedentes só serve se expuser ferramentas de jurisprudência e `verificar_citacoes` (em 13/10/2026 apareceu só com ferramentas de peças e licitação). Se servir, copiar `link_oficial` sem alterar.

## Se nem o plano B achar
Tratar o precedente como não localizado. Nunca completar ementa, relator ou data de memória, nem citar julgado que só apareceu em modelo antigo ou blog. Se for o caso, pedir ao usuário que abra o link oficial no navegador dele e traga o texto.

## O que entregar
Para cada precedente usado: número, classe, relator, órgão julgador, data de julgamento; ementa ou tese literal entre aspas; confirmação objetiva ("confirma", "confirma em parte" ou "não confirma") com o trecho que sustenta; link oficial como veio. Sinalizar precedente contrário ou superado se aparecer.

## Aplicação na minuta (DOCX)
- O revisor altera o texto e explica em comentário lateral; não deixa sugestão para o assessor decidir (C-54, C-55). Texto novo em cinza 808080; IDs e dispositivos ao final do período (C-20). Dispositivo de lei, súmula ou tese vinculante citado ganha comentário lateral com transcrição entre aspas.
- Precedente correto: sem alteração, no máximo comentário curto.
- Precedente que não diz o que a minuta afirma: ajustar a frase ao que ele realmente diz (sem mudar fatos, pedidos ou resultado, C-03, C-24) ou substituir por precedente confirmado, explicando no comentário.
- Não localizado: comentário lateral "não localizado", com a fonte e a consulta feitas; não inventar substituto.

## Economia
Buscar pouco, ler apenas o precedente que será citado.