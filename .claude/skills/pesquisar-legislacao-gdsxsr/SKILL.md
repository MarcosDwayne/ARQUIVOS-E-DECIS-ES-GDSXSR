---
name: pesquisar-legislacao-gdsxsr
description: Busca e confere legislação federal, distrital (DF), atos normativos internos do TJDFT e atos normativos do CNJ nas fontes oficiais (Planalto, SINJ-DF, DFLegis, Diário Administrativo do TJDFT e portal de atos normativos do CNJ), devolvendo o nome e a ementa da norma, o texto literal do dispositivo na redação vigente, a situação de vigência e o link. Usar sempre que o Revisor GDSXSR precisar localizar ou conferir lei, decreto, medida provisória, Constituição, lei distrital, lei complementar do DF, resolução (inclusive do CNJ), portaria, provimento, recomendação ou regimento interno citado numa minuta de voto (APC, AGI, EMD), checar se artigo/número/data estão certos, se a norma foi revogada ou alterada, ou transcrever um artigo, mesmo que o usuário não diga "legislação" nem o nome das fontes.
---

# Pesquisar legislação (GDSXSR)

Esta habilidade localiza a norma nas fontes oficiais e devolve, para cada norma pedida, o que o revisor precisa para conferir a citação de uma minuta. Os sites são a fonte principal; o motivo é que só eles mostram a redação vigente, a situação (revogada, alterada, declarada inconstitucional) e o link oficial que pode ser citado.

## O que devolver

Para cada norma, nesta ordem:

1. **Identificação e nome**: `Lei nº 13.105, de 16 de março de 2015 — Código de Processo Civil`. Use o nome popular ou a ementa curta que a própria fonte traz (no Planalto aparece logo abaixo do título; no SINJ-DF, no campo Ementa e em Apelido).
2. **Ementa** completa, quando a fonte a trouxer (SINJ-DF e DFLegis trazem; no Planalto a ementa é a linha logo após o título).
3. **Dispositivo pedido**, copiado literalmente da fonte, na redação vigente, com a nota entre colchetes de quem alterou (`[Redação dada pela Lei nº 13.256/2016]`). Quando o pedido for só conferir a norma (número, data, ementa), esta parte é dispensada.
4. **Situação**: vigente, alterada, revogada (total/parcial) ou declarada inconstitucional, citando a norma ou a ADI que causou isso.
5. **Fonte**: link da página consultada.
6. **Alertas**: tudo que não bate com o que a minuta cita (número, data, artigo inexistente, texto revogado).

Transcreva o texto da fonte, sem parafrasear nem completar de memória: o revisor vai colar ou comparar, e uma palavra trocada vira erro na minuta. Se não achar a norma ou o dispositivo, diga isso e o que foi tentado; não invente.

## Qual fonte usar

| A norma é... | Fonte | Como |
|---|---|---|
| Federal (CF, lei, lei complementar, decreto, decreto-lei, MPV...) | legislacao.presidencia.gov.br para achar; planalto.gov.br para o texto | Chrome na busca, WebFetch no texto |
| Distrital (lei, LC, decreto, portaria do DF) | SINJ-DF (principal); DFLegis para conferir | Chrome na busca, WebFetch no texto |
| Ato do TJDFT (resolução, portaria, provimento, regimento) | Diário Administrativo do TJDFT (links no portal tjdft.jus.br) | Só Chrome |
| Ato do CNJ (resolução, recomendação, provimento, portaria, instrução normativa, enunciado...) | cnj.jus.br/atos_normativos (busca); atos.cnj.jus.br/atos/detalhar/ID (texto) | Só Chrome |

Em testes, o WebFetch é barrado pelo portal de busca do Planalto e pelo site do TJDFT (acesso automatizado proibido), e não enxerga os resultados do SINJ-DF nem do DFLegis (páginas montadas por JavaScript). Nesses casos use o Claude in Chrome, que lê as páginas como o usuário. Não tente contornar o bloqueio com curl, espelhos ou cache.

Antes de usar o Chrome, leia a habilidade `chrome-browser`, carregue as ferramentas com uma única chamada de ToolSearch, abra uma aba própria e feche-a ao terminar. Se houver mais de um Chrome conectado, pergunte ao usuário qual usar. Se o Chrome não estiver conectado, avise que ele precisa estar aberto com a extensão ativa e siga só com o que o WebFetch alcança.

## Federal

1. No Chrome, abra `https://legislacao.presidencia.gov.br/`, preencha **Número** e **Ano** (só dígitos, ex.: 13105 e 2015), ajuste o tipo se houver ambiguidade e clique em Pesquisar. Se só tiver o nome, use "Busca por termos".
2. O resultado mostra título, data, situação ("Não há revogação expressa", "Revogado"...) e a denominação (ex.: "CÓDIGO DE PROCESSO CIVIL"). Com `find`, pegue o link do texto integral (aponta para `planalto.gov.br/ccivil_03/...`). Use esse link, em vez de montar a URL de cabeça, porque o caminho varia por tipo e período.
3. Leia o texto com WebFetch nesse link (o site planalto.gov.br responde). Peça no prompt só o que precisa (ementa e artigo X).
4. Existe também a versão `...compilada.htm` ("Texto compilado"), útil quando a lei foi muito alterada.

Cuidados com o texto do Planalto:
- A mesma página traz o texto original e o alterado do mesmo artigo (no teste, o art. 12 do CPC apareceu duas vezes). Vale a versão marcada "(Redação dada pela Lei...)" ou o texto compilado; "(Revogado...)" não vale. Leia também as notas "(Vide ADI...)".
- O WebFetch devolve caracteres acentuados corrompidos nesse site (problema de codificação). Corrija os acentos ao transcrever, sem mudar palavras.
- Em leis longas o WebFetch trunca o retorno (o CPC parou perto do art. 231). Para artigos do fim do texto, abra o link com âncora no Chrome (ex.: `...l13105.htm#art1045`) e leia só aquele trecho com `find` ou `javascript_tool`.

## Distrito Federal (SINJ-DF, com conferência no DFLegis)

SINJ-DF:
1. No Chrome, navegue direto para a busca por número e ano, trocando N e AAAA:
   `https://www.sinj.df.gov.br/sinj/ResultadoDePesquisa?tipo_pesquisa=norma&all=&ch_tipo_norma=&nm_tipo_norma=&nr_norma=N&ano_assinatura=AAAA&ch_orgao=&ch_hierarquia=&sg_hierarquia_nm_vigencia=&origem_por=toda_a_hierarquia_em_qualquer_epoca1`
   Sem o tipo, a busca traz todos os tipos com aquele número; escolha pelo título (ex.: "Lei Complementar 840 de 23/12/2011"). Para busca por assunto, use o formulário (Pesquisa Geral ou Pesquisa de Normas).
2. `get_page_text` na lista dá título, selo de situação ("Alterado", "Revogado"...), origem e **ementa**. Isso já basta para conferir número, data e ementa.
3. Para o texto, clique no título (abre `DetalhesDeNorma.aspx?id_norma=ID`). Essa página é enorme porque lista todas as normas que a afetam. Evite ler tudo: use `find` para achar o link "Texto da Norma" (formato `.../sinj/Norma/ID/Tipo_N_dd_mm_aaaa.html`) e leia esse link com WebFetch. Se precisar do histórico (quem alterou o art. X, ADI), aí sim leia a página de detalhes e procure o artigo.
4. No texto, o que está riscado (`~~assim~~` no WebFetch) foi revogado ou substituído e não vale; a redação vigente vem logo abaixo, com a nota "(Artigo Alterado(a) pelo(a) Lei Complementar ...)". Trechos "Declarado(a) Inconstitucional" também estão riscados. Informe isso no campo Situação.
5. Textos longos também são truncados pelo WebFetch (a LC 840/2011 parou perto do art. 155). Para os artigos finais, use o Chrome na mesma URL.

DFLegis (`https://dflegis.df.gov.br/`), usado para conferir ou quando o SINJ-DF não achar: no Chrome, clique na caixa de busca, digite o tipo, número e ano (ex.: `Lei Complementar 840`) e tecle Enter. A busca é por texto livre e traz muitas portarias que apenas citam a norma; a norma procurada costuma vir primeiro, mas confirme pelo título. Cada resultado mostra título, situação ("Sem revogação expressa", "Revogado"), órgão, ementa e os links "Texto Integral" e "Ficha da Norma"; o filtro "Tipo de legislação" à esquerda reduz o ruído. A própria página avisa que o DFLegis é informativo, sem cunho oficial; se SINJ-DF e DFLegis divergirem, relate a divergência.

## Atos normativos do TJDFT

1. No Chrome, abra `https://www.tjdft.jus.br/publicacoes/publicacoes-oficiais/informacoes/atos-normativos`. A página lista os tipos (Resolução do Pleno, Portaria Conjunta, Provimento Geral da Corregedoria, Regimento Interno, Emendas Regimentais etc.), cada um apontando para `https://diarioadministrativo.tjdft.jus.br/arvore-tipos/ID`. Ids vistos: Resolução do Pleno 1342, Portaria Conjunta 191, Provimento Geral da Corregedoria 2050, Regimento Interno 219; para os demais, pegue o link com `find`.
2. Na árvore, expanda o ano clicando na seta à esquerda do ano (clicar no texto não expande). Os atos aparecem como "Resolução do Pleno 1 de 06/02/2026". Confira por **número e ano**: a data da árvore é a de disponibilização e pode ser diferente da data do ato (a Resolução 1/2026 foi disponibilizada em 06/02 e é de 04/02/2026).
3. O botão **Link SEI** abre uma nova aba em `sei.tjdft.jus.br/...publicacao_visualizar...` com o texto do ato; leia com `get_page_text` e feche a aba.
4. O texto do SEI é o ato como foi publicado, não uma versão consolidada. Se o ato pode ter sido alterado (a Resolução 1/2026, por exemplo, acrescenta parágrafo à Resolução 11/2023), procure atos posteriores do mesmo tipo que o mencionem e avise o usuário quando não conseguir confirmar a redação atual.

## Atos normativos do CNJ

O WebFetch recebe 403 no cnj.jus.br e no atos.cnj.jus.br; use só o Chrome.

1. No Chrome, abra `https://www.cnj.jus.br/atos_normativos/`. O formulário de busca fica dentro de um iframe, então `get_page_text`, `read_page` e `find` não o enxergam. Trabalhe com capturas de tela e cliques por coordenada (se a captura vier reduzida, divida as coordenadas pela escala).
2. Marque o tipo desejado (Resolução, Recomendação, Provimento, Portaria, Instrução Normativa etc.), preencha **Número** e **Ano** (ou o campo de argumento/palavras, quando só tiver o assunto) e clique em Pesquisar. Role até a tabela de resultados: tipo, número, data, origem, situação (ex.: "Alterado", "Revogado") e ementa. Isso já basta para conferir número, data, ementa e situação.
3. Para o texto, clique no número do ato. Abre uma nova aba em `https://atos.cnj.jus.br/atos/detalhar/ID`, que o `get_page_text` lê por inteiro. Anote o ID: da próxima vez, navegar direto para essa URL dispensa a busca. Feche a aba ao terminar.
4. A página de detalhe traz identificação, ementa, situação, origem, fonte de publicação (ex.: "DJE/CNJ n. 241/2013"), a lista de atos que alteraram a norma e as abas **Texto Original** e **Texto Compilado**. Prefira o texto compilado para a redação vigente.
5. No texto, leia as marcas: "(Redação dada pela Resolução nº ...)" e "(Incluído pela ...)" valem; "(Revogado pela ...)" não vale. Alguns artigos aparecem duas vezes (original e alterado): vale o que traz "Redação dada".
6. O próprio CNJ avisa que as informações do sistema são informativas, sem caráter oficial. Quando a minuta depender do texto exato, indique a fonte de publicação (DJe/CNJ) no campo Fonte e alerte se não conseguiu confirmá-la.

## Quando algo dá errado

- Se a fonte bloquear (`ROBOTS_DISALLOWED`) ou não carregar, passe para o Chrome. Se o Chrome também falhar duas ou três vezes, pare e conte ao usuário o que tentou, em vez de insistir.
- Se aparecer CAPTCHA, não tente resolver; peça ao usuário.
- Se o ambiente de shell for bloqueado, não repita com outro comando: o bloqueio vale para qualquer rota do shell.
- O iajus (`pesquisar_normas`, `consultar_fonte_oficial` com operação `alteracoes` para saber se a norma foi alterada ou revogada, e `ler_documento` para o texto) apoia a busca e só substitui a fonte oficial se as fontes oficiais estiverem inacessíveis, e o resultado deve sair marcado como "não conferido na fonte oficial".
- Se o usuário pedir várias normas, resolva uma por vez e devolva tudo junto, na ordem em que a minuta as cita.

## Exemplo de saída

**Lei nº 13.105, de 16 de março de 2015 — Código de Processo Civil**
Ementa: Código de Processo Civil.
Art. 12. Os juízes e os tribunais atenderão, preferencialmente, à ordem cronológica de conclusão para proferir sentença ou acórdão. [Redação dada pela Lei nº 13.256/2016]
Situação: vigente, com alterações (a redação original do art. 12 foi substituída).
Fonte: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2015/lei/l13105.htm
Alertas: nenhum.
