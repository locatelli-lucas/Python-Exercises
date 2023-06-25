real = float(input('Qual a sua quantia de dinheiro em real?: R$'))

dolarValue = 5.26
conversão = real / dolarValue
print("Você tem R${:.2f} ou ${:.2f}".format(real, conversão))