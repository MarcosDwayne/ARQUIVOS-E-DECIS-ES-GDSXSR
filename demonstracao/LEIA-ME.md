# Assessor GDSXSR — pacote de demonstração

Este pacote permite montar, na sua própria conta do Claude, uma cópia do "Assessor GDSXSR": um assistente que revisa minutas de voto (apelação, agravo de instrumento e embargos de declaração) no padrão de um gabinete do TJDFT.

**Tudo o que está aqui é material limpo:** não há processos reais, nomes de partes, nomes de assessores nem minutas de casos verdadeiros. Os números de processo aparecem como `0000000-00` e as minutas de teste são inventadas.

## O que você precisa
- Uma conta do Claude com assinatura que permita **Projetos** (Pro, Max, Team ou Enterprise).
- Uma conta Google (para o Google Drive), se quiser usar a pasta de modelos.
- Opcional: acesso ao **iajus** (ferramenta de pesquisa de jurisprudência e leis). Sem ele, o assistente usa as buscas de reserva, que são mais lentas.

## O que tem em cada pasta
| Pasta / arquivo | Para que serve |
|---|---|
| `INSTRUCOES-DO-PROJETO.md` | O texto que vai no campo "Instruções" do projeto |
| `projeto/.claude/skills/` | As 8 "habilidades" (skills) do assistente |
| `projeto/claude/CALIBRACOES-*.md` | As regras de estilo (núcleo + uma por classe: APC, AGI, EMD) |
| `projeto/claude/PERFIL-*.md` | Perfis de estilo de cada classe |
| `projeto/claude/ferramentas/` | Programas auxiliares (controle de alterações, conferência final etc.) |
| `projeto/agente.yaml` | Parâmetros do assistente |
| `modelos-exemplo/INDICE-MODELOS-EXEMPLO.csv` | Exemplo (fictício) do índice de modelos |
| `minutas-ficticias/` | Três minutas inventadas (APC, AGI, EMD) para o primeiro teste |

## Passo a passo

**1. Criar o projeto.** Em claude.ai, clique em **Projetos > Criar projeto**. Dê o nome "Assessor GDSXSR".

**2. Colar as instruções.** Abra `INSTRUCOES-DO-PROJETO.md`, copie o texto que está abaixo da linha e cole no campo **Instruções** do projeto.

**3. Colocar os arquivos no projeto.** Em **Arquivos do projeto**, envie o conteúdo da pasta `projeto/` (as regras `claude/CALIBRACOES-*.md`, os perfis `claude/PERFIL-*.md`, o `agente.yaml` e os programas de `claude/ferramentas/`). Se a plataforma não aceitar pastas, envie os arquivos um a um.

**4. Salvar as skills.** Em **Configurações > Capacidades > Skills** (ou **Personalizar > Skills**), crie uma skill para cada pasta de `projeto/.claude/skills/` enviando o arquivo `SKILL.md` correspondente. São oito: revisar-voto, coerencia-turma, minutar-voto-pje, registrar-calibracao, atualizar-modelos, pesquisar-jurisprudencia, pesquisar-legislacao e ocr-pdf. Se preferir, peça ao próprio Claude: "salve estas skills" e anexe os arquivos.

**5. Conectar o Google Drive.** Em **Configurações > Conectores**, conecte o Google Drive. Crie no seu Drive uma pasta "ASSESSOR GDSXSR" com seus próprios modelos de voto (os do gabinete não estão neste pacote). Quando tiver modelos, o assistente os usa como referência de estilo.

**6. Conectar o iajus.** Em **Configurações > Conectores**, adicione o conector do iajus (mcp.iajus.com.br) e entre com a sua conta. É ele que confirma leis, súmulas e acórdãos.

**7. Testar.** Abra um chat dentro do projeto, anexe uma das minutas de `minutas-ficticias/` e escreva: "Revise esta minuta." O assistente devolve um DOCX revisado, com comentários laterais explicando cada alteração.

## O que esperar e limites
- Este pacote **não inclui** os modelos reais do gabinete, as decisões anteriores nem os perfis por assessor. Os resultados dependem dos modelos que você colocar no seu Drive.
- Algumas skills citam arquivos que ficaram de fora (perfis por assessor e o perfil PASEP). O assistente segue normalmente; ele apenas avisa que não os encontrou.
- Nos textos, `[revisor]` indica a pessoa que corrigiu votos no gabinete de origem, e `assessor` substitui nomes de assessores.
- A revisão é apoio ao trabalho do profissional. Confira sempre o resultado, as citações e os fatos antes de usar qualquer minuta.
