from random import randint
from time import sleep
computador = randint(0, 5)
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5...Tente advinhar!!!')
print('-=-'*20)

jogador = int(input("Qual número você chuta? "))
print("PROCESSANDO")
sleep(3)

if jogador == computador:
    print("PARABÉNS, VOCÊ ACERTOU!!!")
else:
    print("Eu ganhei otário. Eu pensei no número {} e você chutou o número {}".format(computador, jogador))