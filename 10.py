valorCarro = float(60.00)
valorKm = float(0.15)
dias = int(input("Quantos dias alugados? "))
km = float(input("Quantos Km rodados? "))

valorTotal = valorCarro*dias + valorKm*km

print("O total a pagar é de R${:.2f}".format(valorTotal))