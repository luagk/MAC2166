# MAC2166
  Introdução à Computação na Escola Poltécnica
  Terceiro Exercício-Programa
  Prazo de Entrega: 06/07/2021
  Space Invaders

Neste Exercício-Programa (EP) iremos ajudar um programador a finalizar uma versão na
linguagem Python do jogo Space Invaders. Este foi um dos jogos de maior sucesso da
plataforma Arcade no fim da década de 70. No jogo, um atirador fica na base, e deve atingir
todos os alienígenas da tela. 

Neste EP, vamos supor que os alienígenas são triângulos. Para cada alienígena, vocês irão
receber as coordenadas dos três vértices do triângulo. A leitura das coordenadas de cada
alienígena pode ser feita com o método a seguir que já se encontra no padrão esperado
neste EP:

def leAlienigena(numero_alienigena):
coordenadas = input("Alienigena %d: " %(numero_alienigena))
# converte a string lida em uma lista de inteiros
coordenadas = coordenadas.split()
for i in range(0,6):
coordenadas[ i ] = int( coordenadas[ i ] )
# separa as três coordenadas dos vértices do alienígena
v0 = [ coordenadas[0], coordenadas[1] ]
v1 = [ coordenadas[2], coordenadas[3] ]
v2 = [ coordenadas[4], coordenadas[5] ]
return v0, v1, v2
Lembrando que os alienígenas são triângulos, as funções do jogo que vocês precisam
desenvolver serão as seguintes, e seus argumentos e retornos devem ser mantidos:
1. Pontos na borda: Função que recebe as coordenadas dos três vértices de um
triângulo e devolve a quantidade de pontos com coordenadas inteiras da borda
deste triângulo.
def pontosNaBorda(v0, v1, v2):
# v0, v1, v2 são coordenadas dos vértices de um triângulo
return quantidade
2. Soma pontos na borda: Função que devolve a soma da quantidade de pontos com
coordenadas inteiras na borda de todos os triângulos, fazendo uso da função
anterior:
def somaPontosNaBorda(alienigenas):
# alienigenas é uma lista de triângulos
return quantidade
3. Ponto interno: Função que recebe as coordenadas de um ponto, e das
coordenadas dos três vértices de um triângulo e devolve True se o ponto pertencer
ao interior do triângulo, ou False caso contrário. Observação importante: nesta
função, não se considera a borda como interno ao triângulo.
def pontoInterno(ponto, v0, v1, v2):
# ponto é a coordenada do ponto de uma munição
# se ponto for interno:
return True
# caso contrário:
return False
4. Limites de busca: Função que recebe as coordenadas dos três vértices de um
triângulo e devolve as coordenadas de dois vértices - (menor x, menor y) e (maior x,
maior y) - que são, respectivamente, os vértices do extremo inferior e do extremo
superior do retângulo que envolve o triângulo.
def limitesDeBusca(v0, v1, v2):
# v0, v1, v2 são coordenadas dos vértices de um triângulo
return x_min, y_min, x_max, y_max
5. Pontos internos: Função que recebe as coordenadas dos três vértices de um
triângulo, e devolve a quantidade de pontos com coordenadas inteiras no interior
deste um triângulo, fazendo uso da Função 4 para limitar a busca por pontos
internos considerando apenas os pontos do retângulo que envolve o triângulo, e
utilizando Função 3 para verificar se cada coordenada inteira do retângulo pertence
ao interior do triângulo. Assim como na Função 3, não consideramos pontos de
borda como internos nesta função.
def pontosInternos(v0, v1, v2):
# v0, v1, v2 são coordenadas dos vértices de um triângulo
return quantidade
6. Soma pontos internos: Função que devolve a soma da quantidade de pontos com
coordenadas inteiras que são internos de todos os triângulos, fazendo uso da função
anterior.
def somaPontosInternos(alienigenas)
# alienigenas é uma lista de triângulos
return quantidade
