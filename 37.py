import random
from time import sleep
jogador = 0
while jogador != 3:
    jogador = int(input('''Suas opções:
    [ 0 ] PEDRA
    [ 1 ] PAPEL
    [ 2 ] TESOURA
    [ 3 ] PARAR
    Qual a sua jogada? '''))

    print("PEDRA")
    sleep(0.5)
    print("PAPEL")
    sleep(0.5)
    print("TESOURA")
    sleep(0.5)

    if jogador == 0:
        jogador = 'PEDRA'
    elif jogador == 1:
        jogador = "PAPEL"
    elif jogador == 2:
        jogador = "TESOURA"

    lista = ['PEDRA', 'PAPEL', 'TESOURA']
    computador = random.choice(lista)

    if jogador == computador:
        print("\33[35mEMPATOU")
    elif jogador == 3:
        print('Obrigado por jogar!')
        break
    elif jogador == 'PEDRA' and computador == 'TESOURA' or jogador == 'PAPEL' and computador == 'PEDRA' or jogador == 'TESOURA' and computador == 'PAPEL':
        print("{} ganha de {}...\33[32mVOCÊ GANHOU!!!".format(jogador, computador))
    else:
        print("{} ganha de {}...\33[33mVOCÊ PERDEU!!!".format(computador, jogador))
