# Assessor GDSXSR

Repositório oficial do projeto de revisão e redação de votos do Gabinete do Des. Sérgio Rocha (4ª Turma Cível, TJDFT).

- `claude/` — calibrações (núcleo + APC/AGI/EMD), perfis de estilo, índice de modelos e `ferramentas/` (portão `checar_voto.py`, `revisao_tracked.py` etc.).
- `.claude/skills/` — skills do Assessor (revisar, coerência com a Turma, pesquisa de jurisprudência e de legislação, registrar calibração, atualizar modelos, OCR, minutar pelo PJe).
- `agente.yaml` — parâmetros do agente.
- `historico/` — registro de alterações das calibrações e texto integral da v16.
- `docs/` — diagnóstico do projeto (13/10/2026) e instruções enxutas do projeto (24/10/2026).

DOCX de entrega e PDFs de autos não entram no Git (ficam na pasta do projeto). Cada calibração nova é um commit.
