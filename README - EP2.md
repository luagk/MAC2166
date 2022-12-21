# MAC2166
  Introdução à Computação na Escola Poltécnica
  Segundo Exercício-Programa
  Jogo da Afinidade

Neste Exercício-Programa (EP) calcularemos a “afinidade” entre duas pessoas. Para compreender melhor
o jogo, dividimos o enunciado em duas partes.
Parte 1:
Nossa calculadora de afinidade consiste no seguinte. Primeiramente definimos um certo número de
jogadas (numJogadas). Em cada jogada, cada pessoa digita um número inteiro positivo. Por exemplo, n1
= 19011981 e n2 = 20021979. Então, a calculadora soma todos os dígitos de n1 e de n2 até que cada um
deles seja composto por apenas um dígito. Por exemplo, para n1 temos que 1+9+0+1+1+9+8+1 = 30 = 3 +
0 = 3. Para n2 temos que 2 + 0 + 0 + 2+ 1+ 9 + 7 + 9 = 30 = 3 + 0 = 3. Após reduzir os números dos dois
jogadores em apenas um dígito, comparamos. A afinidade entre duas pessoas é dada pelo número de
vezes que n1 e n2 foram iguais após a redução para um dígito (numAcertos), dividido por numJogadas.
Ou seja, nesse caso:
afinidade = numAcertos / numJogadas
Parte 2:
Para o cálculo da afinidade, pode-se também considerar a aleatoriedade. Suponha que dois
indivíduos não tenham nenhuma afinidade, mas por uma questão de "sorte", obtiveram uma alta afinidade.
Então nós gostaríamos de considerar no cálculo da afinidade, este fator "sorte". Para isso, após o fim do
jogo pedido na Parte 1, pergunte se o usuário deseja avaliar o fator "sorte". Vamos gerar números
aleatórios e simular dois jogadores virtuais sem afinidade. E com isso, avaliar se os dois jogadores reais
têm de fato afinidade ou não.
Nesta parte 2 do EP, simule as numJogadas dos dois indivíduos gerando números aleatórios n1’
e n2’, usando o método das congruências lineares (explicado mais adiante). Calcule o número de vezes
em numJogadas que n1’ e n2’ foram iguais após a redução para um dígito (numAcertos’). Repita este
processo 10.000 (dez mil) vezes e calcule p, i.e., a proporção em que numAcertos’ é maior ou igual que
numAcertos (obtido na Parte 1). A afinidade dos dois jogadores levando em consideração o fator "sorte" é
dada por um menos p, isto é:
p = (Quantidade de vezes em que numAcertos’ >= numAcertos) / 10000
afinidade = 1 - p
Note que p é a proporção em que a afinidade (obtida na Parte 1) tenha um valor igual ou maior
que no caso em que ambos os jogadores (virtuais) não tem afinidade (os números gerados são aleatórios).
Em outras palavras, esta é a probabilidade de dizermos que os dois jogadores têm afinidade supondo que
eles não tem. Então 1-p pode ser interpretado como a afinidade entre os jogadores levando em conta o
fator "sorte" ou aleatoriedade.
Perceba que você usará somente uma das duas fórmulas para o cálculo da afinidade, a depender
se o usuário desejar simular um novo jogo utilizando números aleatórios (Parte 2) ou não (somente o jogo
inicial descrito na Parte 1).
Ao final do programa, exiba a afinidade calculada sem limitar as casas decimais ou usar alguma
formatação específica (veja os exemplos de execução do programa a seguir), além de uma mensagem
personalizada de acordo com a faixa de afinidade:
● Maior ou igual a 0 e menor que 1/3: “A afinidade de voces e baixa. Que pena!”
● Maior ou igual a 1/3 e menor que 2/3: “A afinidade de voces e mediana!”
● Maior ou igual a 2/3 (caso contrário aos anteriores): “Parabens! Voces tem uma bela afinidade!”

# Exemplos de Execução do Programa
  Nos exemplos, tudo que aparece em negrito foi digitado pelo usuário. Os demais textos foram
  impressos pelo programa.
  Exemplo 1
  Digite o numero de jogadas: 2
  Pessoa 1: digite um numero: 443
  Pessoa 2: digite um numero: 902
  Pessoa 1: digite um numero: 10
  Pessoa 2: digite um numero: 11
  Deseja simular jogadas aleatorias (S/N)? N
  A afinidade de voces e de 0.5
  A afinidade de voces e mediana!
  Exemplo 2:
  Digite o numero de jogadas: 1
  Pessoa 1: digite um numero: 1868388945
  Pessoa 2: digite um numero: 9086721345
  Deseja simular jogadas aleatorias (S/N)? N
  A afinidade de voces e de 0.0
  A afinidade de voces e baixa. Que pena!
  Exemplo 3:
  Digite o numero de jogadas: 3
  Pessoa 1: digite um numero: 653
  Pessoa 2: digite um numero: 131
  Pessoa 1: digite um numero: 280
  Pessoa 2: digite um numero: 775
