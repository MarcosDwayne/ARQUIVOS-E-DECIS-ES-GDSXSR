# Ambiente e conferência jurídica (Assessor GDSXSR)

**Fonte única do escalonamento: C-72 (núcleo).** Resumo operacional, para as skills e perfis só remeterem a esta página:

1. iajus: `pesquisar_decisoes`, `pesquisar_precedentes`, `pesquisar_normas`, `consultar_fonte_oficial`, `ler_documento`.
2. Skills de plano B: `pesquisar-jurisprudencia-gdsxsr` e `pesquisar-legislacao-gdsxsr`.
3. Busca na web (Google ou Bing), até o texto na fonte oficial ou, na falta dela, em fonte confiável que reproduza o acórdão ou a norma.
4. Extensão Claude no Chrome (skill `chrome-browser`), abrindo direto o portal oficial (JurisDF, SCON/STJ, STF, Planalto, SINJ-DF), se as ferramentas do navegador estiverem na thread.
Limite das vias 3 e 4: **até 3 tentativas por citação, somadas**, cada uma com termos novos (processo, relator, órgão, data, tema); conferida a citação, parar.
5. Esgotado o limite sem conferir: citação pendente, uma linha sobre o que foi tentado e o que falhou, e comentário lateral (C-52). Nunca completar processo, relator, data ou tese de memória, nem entregar não conferida como conferida. Dizer o Direito só para descoberta (C-60).

**Ferramentas locais** (`claude/ferramentas/`): `revisao_tracked.py` e `checar_voto.py` (edição rastreada e portão), `aceitar_autor.py` (entrega), `buscar_modelos.py` (filtra o índice de modelos; nunca ler o CSV inteiro), `equivalencia_regras.py` (teste: nenhuma regra C-xx some numa refatoração).
