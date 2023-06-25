from math import floor
n = int(input('Digite um número: '))
base = int(input("Converter para qual base?\n[ 1 ] BINÁRIO\n[ 2 ] OCTADECIMAL\n[ 3 ] HEXADECIMAL\nSua opção: "))

if base == 1:
    
    divisao0 = (n % 2)
    lista = []
    string0 = str(divisao0)
    lista.append(string0)
    num = n
    while num != 1: 
        num = floor(num / 2)
        restoBinario = floor(num % 2)
        string = str(restoBinario)
        lista.append(string)
    lista.reverse()
    newList = "".join(lista)
    print(newList)

elif base == 2:
    
    divisao0 = (n % 8)
    lista = []
    string0 = str(divisao0)
    lista.append(string0)
    num = n
    while num > 8:
        num = floor(num / 8) 
        restoOctal = floor(num % 8)
        string = str(restoOctal)
        lista.append(string)
    lista.reverse()
    newList = "".join(lista)
    print(newList)

else:
    
    divisao0 = (n % 16)
    lista = []
    string0 = str(divisao0)
    lista.append(string0)
    num = n
    while num > 16:
        num = floor(num / 16) 
        restoHex = floor(num % 16)
        string = str(restoHex)
        lista.append(string)
    lista.reverse()
    for i in lista:
        if i == '10':
            lista[lista.index('10')] = "A"
        elif i == '11':
            lista[lista.index('11')] = "B"
        elif i == '12':
            lista[lista.index('12')] = "C"
        elif i == '13':
            lista[lista.index('13')] = "D"
        elif i == '14':
            lista[lista.index('14')] = "E"
        elif i == '15':
            lista[lista.index('15')] = "F"
    newList = "".join(lista)
    print(newList)
