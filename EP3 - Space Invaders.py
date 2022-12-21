" 
 Para rodar o jogo, é necessário instalar o PyGame utilizando o comando:

 $ python -m pip install pygame

 Depois, coloque os arquivos ep03.py e o arquivo space-invaders.py na mesma pasta.

 Dentro da pasta inicie o jogo a partir do comando:

 $ python space-invaders.py
"

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

    #AUXILIARES
def modulo (numero):
    return (numero**2)**(1/2)

def MDC(a, b):
    if a < b:
        a,b = b,a
    while b > 0:
        r = a % b
        a = b
        b = r
    return a


def pontosNaReta (v0,v1):
    quantidade = 0
    m = 1
    if (v0[0] - v1[0]) != 0:
        m = v0[1] - v1[1] / (v0[0] - v1[0])
    if m == 0:
        quantidade += modulo(v0[0] - v1[0])
    elif v0[0] == v1[0]:
        quantidade += modulo(v0[1] - v1[1])
    else:
        quantidade += MDC(modulo(v0[0] - v1[0]), modulo(v0[1] - v1[1]))
    return quantidade

def det(m,n):
    det = (m[0]*n[1]) - m[1]*n[0]
    return det

def coord(): 
    coordenadas = input('Coordenadas do ponto:')
    x = coordenadas.split()[0]
    y = coordenadas.split()[1]
    v = (int(x), int(y))
        
    return v

    #PRINCIPAIS

# Funcao 1 - Quantidade de pontos na borda
def pontosNaBorda(v0, v1, v2):
    # v0, v1, v2 são coordenadas dos vértices de um triângulo
    return pontosNaReta(v0,v1) + pontosNaReta(v1,v2) + pontosNaReta(v2, v0) 

# Funcao 2 - Soma pontos na borda
def somaPontosNaBorda(alienigenas):
    # alienigenas é uma lista de triângulos
    quantidade = 0
    for alienigena in alienigenas:
        v0, v1, v2 = alienigena
        quantidade+= pontosNaBorda(v0, v1, v2)

    return quantidade
        

# Funcao 3 - Ponto interno
def pontoInterno(ponto, v0, v1, v2):
    v1_ = [(v1[0]-v0[0]), (v1[1]-v0[1])]
    v2_ = [(v2[0]-v0[0]), (v2[1]-v0[1])]
    a = ((det(ponto, v2_) - det(v0, v2_)) / det( v1_, v2_ ))
    b = (-(det(ponto, v1_) - det(v0, v1_ )) / det( v1_, v2_ ))
    # ponto é a coordenada do ponto de uma munição
    # se ponto for interno:
    if a>0 and b>0 and (a+b)<1:
        return True
    # caso contrário:
    else:
        return False

# Funcao 4 - Limite de busca
def limitesDeBusca(v0, v1, v2):
    # v0, v1, v2 são coordenadas dos vértices de um triângulo
    x_list = [v0[0],v1[0],v2[0]]
    y_list = [v0[1],v1[1],v2[1]]

    x_max = 0
    x_min = x_list[0]
    for x in x_list:
        if x > x_max:
            x_max = x
        elif x < x_min:
            x_min = x

    y_max = 0
    y_min = y_list[0]
    for y in y_list:
        if y > y_max:
            y_max = y
        elif y < y_min:
            y_min = y

    return x_min, y_min, x_max, y_max

# Funcao 5 - Pontos internos
def pontosInternos(v0, v1, v2):
    x_min, y_min, x_max, y_max = limitesDeBusca(v0, v1, v2)
    lista = [0,0]
    quantidade = 0
    for r in range (x_min, x_max): #(r = x, t=y)
        lista[0]=r
        for t in range (y_min, y_max):
            lista[1] = t
            if pontoInterno(lista, v0, v1, v2):
                quantidade +=1 
    # v0, v1, v2 são coordenadas dos vértices de um triângulo
    return quantidade

# Funcao 6 - Soma pontos internos
def somaPontosInternos(alienigenas):
    quantidade = 0
    for alienigena in alienigenas:
        v0, v1, v2 = alienigena
        quantidade+= pontosInternos(v0, v1, v2)

    return quantidade

# Codigo para executar os testes:
def main():
    alienigenas = []
    n = int(input("Quantidade de alienigenas: "))
    for i in range(0, n):
        alienigenas.append(leAlienigena(i))
    
    teste = int(input('Digite a funcao que deseja testar:')) #DPS DE TER OS PONTOS
    while teste !=0:
        
        if teste == 1:
            numero_alienigena = int(input('Numero do alienigena:'))
            v0, v1, v2 = alienigenas[numero_alienigena]
            print(f'Quantidade de pontos na borda: {pontosNaBorda(v0, v1, v2):.0f}')
            

        elif teste == 2:
            print(f'Soma de pontos na borda: {somaPontosNaBorda(alienigenas):.0f}')

        elif teste == 3:
            ponto = 0
            numero_alienigena = int(input('Numero do alienigena:'))
            x0 = alienigenas [numero_alienigena][0][0]
            y0 = alienigenas [numero_alienigena][0][1]
            x1 = alienigenas [numero_alienigena][1][0]
            y1 = alienigenas [numero_alienigena][1][1]
            x2 = alienigenas [numero_alienigena][2][0]
            y2 = alienigenas [numero_alienigena][2][1]
            print(f'Coordenadas do alienigena: ({x0},{y0}), ({x1},{y1}), ({x2},{y2})')
            v0, v1, v2 = (x0,y0),(x1,y1),(x2,y2)
            ponto = coord()
            if pontoInterno(ponto, v0, v1, v2):
                print('Ponto interno ao triangulo!')
            else:
                print('Ponto nao interno ao triangulo')


        elif teste == 4:
            numero_alienigena = int(input('Numero do alienigena:'))
            v0, v1, v2 = alienigenas[numero_alienigena]
            x_min, y_min, x_max, y_max = limitesDeBusca(v0, v1, v2)
            print(f'Os limites são: ({x_min},{y_min}) e ({x_max},{y_max})')

        elif teste == 5:
            numero_alienigena = int(input('Numero do alienigena:'))
            v0, v1, v2 = alienigenas[numero_alienigena]
            
            print('Quantidade de pontos internos: ', pontosInternos(v0, v1, v2))



        elif teste == 6:
            print('Soma de pontos internos: ', somaPontosInternos(alienigenas))
        teste = int(input('Digite a funcao que deseja testar:'))


    

   



if __name__ == '__main__':
    main()
