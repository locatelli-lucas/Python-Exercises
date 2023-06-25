import random
n1 = input('Digite o nome: ')
n2 = input('Digite o nome: ')
n3 = input('Digite o nome: ')
n4 = input('Digite o nome: ')

nomes = [n1, n2, n3, n4]
random.shuffle(nomes)

print('Os nomes sorteados são {}'.format(nomes))
