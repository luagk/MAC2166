## parâmetros para o método das congruências lineares:
m = 2**32
a = 22695477
c = 1
anterior = 42

num_jogadas = int(input("Digite o numero de jogadas: "))
i = 0
num_acertos = 0

while(i != num_jogadas):
    soma1 = 0
    soma2 = 0
    numero1 = int(input("Pessoa 1: digite um numero:"))
    numero2 = int(input("Pessoa 2: digite um numero:"))

    while(numero1 > 0):
        k1 = numero1 % 10
        soma1 += k1
        numero1 = numero1 // 10
        if soma1 > 9 and numero1 == 0:
            numero1 = soma1
            soma1 = 0
    
    while(numero2 > 0):
        k2 = numero2 % 10
        soma2 += k2
        numero2 = numero2 // 10
        if soma2 > 9 and numero2 == 0:
            numero2 = soma2
            soma2 = 0

    if soma1 == soma2:
        num_acertos += 1

    i += 1

b = input("Deseja simular jogadas aleatorias (S/N)?")

if b == "N":
    afinidade = num_acertos / num_jogadas

if b == "S":
    
    j = 0
    contador = 0
    while j < 10000:
        _i = 0
        num_acertos2 = 0
        _soma1 = 0
        _soma2 = 0
    
        
        while _i <= num_jogadas:
            numero1_ = (a * anterior + c) % m
            anterior = numero1_
            numero2_ = (a * numero1_ + c) % m
            anterior = numero2_

            while numero1_ > 0:
                _k1 = numero1_ % 10
                _soma1 += _k1
                numero1_ = numero1_ // 10
                if _soma1 > 9 and numero1_ == 0:
                    numero1_ = _soma1
                    _soma1 = 0
            
            while numero2_ > 0:
                _k2 = numero2_ % 10
                _soma2 += _k2
                numero2_ = numero2_ // 10
                if _soma2 > 9 and numero2_ == 0:
                    numero2_ = _soma2
                    _soma2 = 0
        
            if _soma1 == _soma2:
                num_acertos2 += 1
        
            _i += 1
            _soma1 = 0
            _soma2 = 0
        j += 1


        if (num_acertos2 >= num_acertos):
            contador += 1
        num_acertos2 = 0
    p = contador / 10000
    afinidade = 1 - p
    
print('A afinidade de voces e de', afinidade)
if afinidade < 1/3:
    print('A afinidade de voces e baixa. Que pena!')
if afinidade >= 1/3 and afinidade < 2/3:
    print('A afinidade de voces e mediana!')
if afinidade >= 2/3:
    print('Parabens! Voces tem uma bela afinidade!')
