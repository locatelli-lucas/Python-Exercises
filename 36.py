preco = float(input('Qual o valor a ser pago? R$'))
formaPagamento = int(input("""[ 1 ] à vista - dinheiro/cheque
[ 2 ] à vista - cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão

Qual é a opção? """))

if formaPagamento == 1:
    valorFinal = preco - preco * 0.1
    print("""Sua compra será à vista com um desconto de 10%!!!
O valor da sua compra de R${:.2f} vai custar R${:.2f}""".format(preco, valorFinal))
elif formaPagamento == 2:
    valorFinal = preco - preco * 0.05
    print("""Sua compra será à vista com um desconto de 5%!!!
O valor da sua compra de R${:.2f} vai custar R${:.2f}""".format(preco, valorFinal))
elif formaPagamento == 3:
    valorParcelas = preco / 2
    valorFinal = preco
    print("""Sua compra será em 2x de R${:.2f} no cartão SEM DESCONTOS!!!
O valor da sua compra é R${:.2f}""".format(valorParcelas ,preco))
else: 
    parcelas = int(input("Quantas parcelas? "))
    valorParcelas = (preco / parcelas) * 1.2
    valorFinal = preco * 1.2
    print("""Sua compra será em {}x de R${:.2f} no cartão COM JUROS!!!
O valor da sua compra de R${:.2f} vai custar R${:.2f}""".format(parcelas, valorParcelas ,preco, valorFinal))

