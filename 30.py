casaValor = float(input('Qual o valor da casa? R$'))
salarioComprador = float(input("Qual o salário do comprador? R$"))
anosPagando = int(input("Em quantos anos pretende pagar? "))

prestaçaoMensal = casaValor/(anosPagando*12)

if prestaçaoMensal > salarioComprador * 1.3:
    print("Para pagar uma casa de R${:.2f} em {} anos, a prestação será de R${:.2f}".format(casaValor, anosPagando, prestaçaoMensal))
    print("\33[4;31mPRESTAÇÃO NEGADA!!!")
else:
    print("Para pagar uma casa de R${:.2f} em {} anos, a prestação será de R${:.2f}".format(casaValor, anosPagando, prestaçaoMensal))
    print("\33[4;32mPRESTAÇÃO APROVADA")

