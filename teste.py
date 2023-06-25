lista = ['10', '11', '12', '13', '14', '15']

for i in lista:
    if i == '10':
        lista[lista.index('10')] = "A"
    elif i == '11':
        i = "B"
    elif i == '12':
        i = "C"
    elif i == '13':
        i = "D"
    elif i == '14':
        i ="E"
    elif i == '15':
        i ="F"
print(lista)
