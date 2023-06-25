n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
n3 = int(input('Digite um número: '))

lista = [n1, n2, n3]
listaSorted = lista
listaSorted.sort()

print("O menor número é {}".format(listaSorted[0]))
print("O maior número é {}".format(listaSorted[listaSorted.__len__()-1]))