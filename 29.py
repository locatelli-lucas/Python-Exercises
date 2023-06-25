salario = float(input("Qual o seu salário? R$"))
aumento = salario

if salario > 1250:
    aumento = salario * 1.1
else:
    aumento = salario * 1.15

print("O seu salário foi de {}{:.2f}{} para {}{:.2f}".format('\33[4;31mR$', salario, '\33[m','\33[4;32mR$',aumento))