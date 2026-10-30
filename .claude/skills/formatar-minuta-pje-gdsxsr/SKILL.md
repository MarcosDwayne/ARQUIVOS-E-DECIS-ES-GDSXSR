---
name: "formatar-minuta-pje-gdsxsr"
description: "Depois que o Desembargador aprovou a minuta, confere e reaplica a formatação direta da ementa, do relatório e do voto no Word (Arial, recuos, entrelinha, parágrafos vazios, barra separadora, rodapé da ementa, espaço não separável, cinza 595959 para cor automática) para que o texto copiado chegue ao PJe sem desformatar, sem alterar nenhum caractere. Usar quando o usuário pedir para formatar, preparar ou conferir a minuta aprovada para gravar no PJe."
---

# Formatar a minuta aprovada para o PJe (GDSXSR)

## Escopo
Esta skill entra depois que o desembargador aprovou a minuta e a devolveu para registro no PJe. O texto está congelado. Só a ementa, o relatório e o voto são copiados e colados no PJe; o resto do arquivo serve à identificação do processo e ao trabalho do desembargador.

## Regra zero — área de trabalho e limites
**Área de trabalho:** ementa, relatório e voto (dispositivo incluído).

**Pode ser alterado, dentro da área de trabalho:** a cor de fonte cinza 595959, que passa a automática (e nenhuma outra cor), fonte, tamanho, espaçamento entre linhas, espaçamento antes/depois do parágrafo, alinhamento, recuo, itálico, negrito, "Manter com o próximo" e a presença do parágrafo vazio entre parágrafos. A barra separadora da ementa é elemento de formatação: restaurá-la está autorizado.

**Não pode ser alterado:** nenhum caractere do texto. Nem palavra, nem pontuação, nem acento, nem caixa, nem numeração, nem ordem de parágrafos. Nada é acrescentado nem suprimido. A única exceção é a do item 2.8: trocar espaço não separável por espaço comum, que substitui um caractere invisível por outro sem mudar uma letra do que está escrito.

**Erro de conteúdo não se corrige.** Se aparecer erro de conteúdo (palavra vetada, numeração da ementa reiniciada, item 1 da ementa abrindo pelo recurso, ementa mais detalhada que o voto), não corrija. Anote e relate ao final, para a usuária decidir se devolve a minuta à revisão.

Esta skill só cuida da formatação das três peças que vão ao PJe, depois da aprovação.

<!-- PENDENTE: a "Regra zero" original também traz a lista dos sete nomes proibidos no relatório (citada no Passo 4). Colar a lista aqui. -->

## Passo 1 — Contexto de execução
Esta skill roda dentro do Word, pelo add-in, com a minuta aprovada já aberta. Não peça anexo, não peça upload e não trabalhe sobre cópia.

Se, por exceção, a minuta vier como texto colado no chat, pare: fonte, recuo e espaçamento não existem nesse meio. Nunca afirme ter conferido formatação em texto de chat.

Antes de começar, ative "Mostrar tudo" (Ctrl+Shift+8) — parágrafos vazios a mais ou a menos e quebras indevidas só aparecem com as marcas visíveis.

## Passo 2 — Conferência e reaplicação
Oito itens, aplicados só dentro da área de trabalho da Regra zero. Percorra todos antes de corrigir qualquer um. O item 2.7 é exceção e tem regra própria: não se confere, aplica-se direto.

### 2.1 — Reaplicar a formatação explicitamente, bloco a bloco, mesmo quando parecer correta
Esta é a causa raiz da desformatação no PJe e não há como diagnosticá-la só olhando: o Word mostra na barra a fonte herdada do estilo exatamente como mostra a aplicada diretamente, mas só a aplicada diretamente sobrevive ao Ctrl+C. O editor do PJe descarta a folha de estilo e preserva apenas a formatação direta.

Selecione cada bloco e reaplique fonte, tamanho, espaçamento e alinhamento — nunca as três peças de uma vez, sob pena de achatar as diferenças entre corpo, títulos, transcrições e rodapé:

| Bloco | Fonte | Alinhamento | Recuo |
|---|---|---|---|
| Corpo do relatório e do voto | Arial 14 | justificado | 1ª linha 4,0 cm |
| Ementa — cabeçalho de indexação, títulos I a IV e itens numerados | Arial 14 | justificado | sem recuo |
| Títulos do voto (EMENTA, RELATÓRIO, VOTO, DISPOSITIVO e os títulos de capítulo) | Arial 14 | centralizado | sem recuo |
| Transcrições dentro do relatório ou do voto | Arial 13 itálico | justificado | 1ª linha 6, demais 4 |
| Citações de ementa, acórdão e dispositivo legal | Arial 13 itálico | justificado | bloco de 4, tudo alinhado |
| Barra separadora da ementa | Arial 14 | à esquerda | sem recuo |
| Rodapé da ementa | Arial 13 | justificado | sem recuo |

**A ementa não leva recuo em parágrafo nenhum** — nem o cabeçalho de indexação, nem os títulos I a IV, nem os itens numerados, nem a barra, nem o rodapé. O recuo de 4 cm é do corpo do relatório e do voto, e só deles.

Este é o erro mais fácil de cometer aqui, porque a régua do corpo parece geral e a ementa está logo acima: ao reaplicar o recuo bloco a bloco, é ela que acaba recebendo um recuo que nunca teve. (Corrigido na auditoria de 19/09/2026, quando esta tabela ainda reunia ementa, relatório e voto numa linha só.)

Parágrafo vazio recebe fonte e espaçamento diretos — não o deixe de fora da seleção. Alinhamento em parágrafo vazio é indiferente: não o exija nem o relate como divergência.

### 2.2 — Espaçamento entre linhas 1,5
Parágrafo → Espaçamento entre linhas: "1,5 linhas". Vale em toda a área de trabalho: corpo, títulos, transcrições, ementa, rodapé e parágrafos vazios. Reaplique mesmo onde já estiver correto, pelo motivo do item 2.1.

### 2.3 — Espaçamento "Depois" do parágrafo em 0 pt
No relatório e no voto é indispensável: como a separação vem do parágrafo vazio, qualquer valor remanescente dobra o afastamento.

### 2.4 — Parágrafo vazio entre parágrafos, só no relatório e no voto
Entre dois parágrafos do relatório ou do voto (dispositivo incluído) há um parágrafo vazio, inclusive antes e depois de cada transcrição. Exceção interna: parágrafos de uma mesma citação seguem colados entre si.

A ementa não recebe parágrafo vazio em ponto algum — cabeçalho de indexação, itens I a IV, barra e rodapé vão direto um após o outro. Não confunda com o espaçamento 1,5 dentro do parágrafo, que vale em tudo.

Com "Mostrar tudo" ativo, conte as marcas de parágrafo: uma sozinha entre dois blocos de texto no relatório e no voto, nenhuma dentro da ementa.

### 2.5 — Barra separadora da ementa
Exatamente 10 caracteres underline, em parágrafo próprio, Arial 14, sem recuo, com alinhamento à esquerda aplicado explicitamente — clique no parágrafo e acione "Alinhar à esquerda" mesmo que ele já pareça alinhado. Parecer alinhado não basta: se o alinhamento vier herdado do estilo, ele não sobrevive ao Ctrl+C e a barra chega ao PJe justificada, esticada de margem a margem. Já aconteceu em minuta gravada.

Conte os underlines um a um: 6, 8, 9 e 12 são visualmente parecidos e todos errados — 9 já passou despercebido em minuta real.

Se a barra estiver como borda inferior de parágrafo em vez de underlines (efeito da autocorreção do Word), remova a borda em Parágrafo → Bordas e digite os 10 underlines. Desative a autoformatação que reconverte underlines em borda antes de digitar, senão ela volta.

### 2.6 — Rodapé da ementa
Os dois blocos, "Dispositivos relevantes citados:" e "Jurisprudência relevante citada:", em Arial 13, justificados, em parágrafos consecutivos e colados, sem linha em branco entre eles, sem recuo de primeira linha, com o rótulo em itálico e o conteúdo em texto normal. Confira o tamanho selecionando o texto e lendo o valor na barra — Arial 13, nunca 14. Se o voto não citou precedente, o bloco de jurisprudência não existe: rótulo e tudo.

### 2.7 — "Manter com o próximo" na barra e no bloco de dispositivos
Sem isso a barra fica órfã no pé da página e o rodapé cai sozinho na seguinte.

Já se constatou na prática que o add-in não lê essa propriedade. Não tente conferi-la, não diga que não conseguiu conferir e nunca a declare conforme.

Em vez de conferir, aplique às cegas: marque "Manter com o próximo" (Parágrafo → Quebras de linha e de página) na barra separadora e no parágrafo "Dispositivos relevantes citados:". Marcar o que já está marcado não altera nada, então aplicar sem conhecer o estado anterior é seguro.

Se também não for possível aplicar, encerre o relatório com esta linha, sem rodeios: "'Manter com o próximo' não pode ser aplicado por aqui — marque a mão na barra separadora e no bloco de dispositivos, em Parágrafo → Quebras de linha e de página, antes de gravar." Esse aviso não impede a frase de sucesso.

### 2.8 — Bolinhas: espaço não separável e marcador de lista
São duas coisas diferentes, com tratamento diferente. Confira as duas mesmo que as marcas de formatação estejam desligadas — o defeito existe esteja ele visível ou não.

**Espaço não separável** — o Word o exibe como um círculo elevado (°) quando "Mostrar tudo" está ligado. Costuma entrar colado de PDF ou de outro editor e bagunça quebra de linha e justificação no PJe. Substitua todos por espaço comum dentro da área de trabalho: Localizar e Substituir, com `^s` no campo de busca e um espaço comum no de substituição. É a única alteração de caractere autorizada nesta skill, e é segura: troca um caractere invisível por outro, sem mudar uma letra do que está escrito. Diga no relatório quantos foram trocados.

**Marcador ou numeração automática de lista** — a bolinha ou o número que o Word insere sozinho, em vez de digitado no texto. A numeração da ementa é para ser digitada; lista automática renumera ou some ao colar no PJe. Não remova: tirar a formatação de lista apaga os números junto, e repor os números seria alterar o texto. Relate onde encontrou e avise que precisa ser convertido à mão antes de gravar. Para identificar, clique no parágrafo e veja se o botão de lista da faixa está aceso.

**Referência dos valores:** `references/manual-gabinete.md` da skill minuta-cível, seção "Formatação Word", e `references/ementa-estruturada.md`, seção "Formatação da ementa". (Neste repositório, ver também `claude/CALIBRACOES-FORMATACAO-GDSXSR.md`, C-40 a C-48.)

## Passo 3 — Corrigir
Corrija no próprio documento aberto, bloco a bloco, sem tocar em nenhum caractere do texto e sem sair da área de trabalho. Conferir e não corrigir não cumpre a tarefa: a skill existe para entregar o documento pronto, não uma lista de defeitos.

Depois de corrigir, percorra o Passo 2 outra vez do começo: reaplicar formatação em um bloco às vezes desfaz recuo ou espaçamento do bloco vizinho.

Não salve versão paralela nem renomeie o arquivo, salvo se a usuária pedir.

## Passo 4 — Relatar
Antes de escrever a resposta, releia a Regra zero e confira se nenhum dos sete nomes proibidos entrou no texto. Se entrou, refaça.

- **Nenhuma divergência:** diga exatamente "A minuta está pronta para ser gravada no PJe" e lembre que vão para o PJe apenas a ementa, o relatório e o voto, copiados e colados, e que o editor do PJe não tem controle de entrelinha para corrigir nada depois — o que for colado é o que fica.
- **Com divergências:** liste cada uma pelo número do item do Passo 2, dizendo em que peça e em que parágrafo apareceu e o que foi corrigido. Só então diga que está pronta.
- **Divergências de conteúdo** encontradas de passagem: liste em bloco separado, marcadas como não corrigidas, e pergunte se a usuária quer devolver a minuta à revisão antes de gravar.

Nunca use a frase de sucesso sem ter percorrido os itens 2.1 a 2.6 e 2.8, providenciado o 2.7 na forma prevista ali e convertido o cinza 595959 em cor automática em toda a área de trabalho (Regra zero).
