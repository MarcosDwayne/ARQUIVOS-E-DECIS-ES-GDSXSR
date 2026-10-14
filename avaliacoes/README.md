# Avaliações do Assessor GDSXSR

Objetivo: medir se uma mudança em calibração, skill ou ferramenta melhora ou piora a revisão. Cada caso é uma minuta conhecida, com a versão final do Des. Sérgio Rocha como gabarito.

## Como montar um caso (3 a 5 casos, de classes diferentes)
1. Crie `avaliacoes/casos/NOME-DO-CASO/` e coloque nela `original.docx` (minuta crua), `final.docx` (versão do Desembargador) e `esperado.md` (o que a revisão deve fazer, em poucas linhas: resultado, citações que devem ser confirmadas, alterações que não podem faltar).
2. Registre o caso em `avaliacoes/casos.json`.

## Como rodar
1. Revise `original.docx` com a skill revisar-voto-gdsxsr e salve o resultado como `agente.docx` na pasta do caso.
2. `python3 avaliacoes/avaliar.py` — roda o portão (`checar_voto.py`) e a comparação com a versão final (`comparar_versoes.py`) em cada caso e imprime um resumo.
3. Compare o resumo com o anterior antes de aprovar a mudança.

## O que olhar
- Portão sem ERRO.
- Alterações do agente que sobreviveram na versão final (quanto mais, melhor).
- Itens de `esperado.md` atendidos (conferência manual).
