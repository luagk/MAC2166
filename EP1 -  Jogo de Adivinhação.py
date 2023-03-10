"""
  MAC2166 - ESCOLA POLITÉCNIC DA USP
"""

# sorteia um número inteiro no intervalo [1,20]
import random
semente = int(input("Digite a semente do sorteio: "))
random.seed(semente)
numero_sorteado = random.randint(1,20)

print('Escolhi um inteiro entre 1 e 20. Adivinhe-o!')
tentativa = 0
acertou = 0
while tentativa < 5 and acertou == 0:
    tentativa += 1
    chute = int(input('Seu chute: '))
    if chute > numero_sorteado:
        print('Chutou alto')
        if chute % 2 == 0 and numero_sorteado % 2 != 0:
            print('Tente um impar')
        if chute % 2 != 0 and numero_sorteado % 2 == 0:
            print('Tente um par')
    elif chute < numero_sorteado:
        print('Chutou baixo')
        if chute % 2 == 0 and numero_sorteado % 2 != 0:
            print('Tente um impar')
        if chute % 2 != 0 and numero_sorteado % 2 == 0:
            print('Tente um par')
    else:
        print('Legal, acertou na tentativa', tentativa)
        acertou += 1

if tentativa >= 5:
    print('Tentativas esgotadas!')
    print('O escolhido foi o', numero_sorteado)
