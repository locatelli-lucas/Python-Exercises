salario = float(input('Qual o salário do funcionário? R$'))
aumento = float(0.15)
salarioFinal = salario + salario*aumento

print('Um funcionário que ganhava R${}, com {:.0f}% de aumento, passa a receber R${:.2f}'.format(salario, aumento*100, salarioFinal))