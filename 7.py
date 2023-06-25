preco = float(input('Qual o preço do produto? R$'))
desconto = float(0.05)
valor = preco - preco*desconto

print('O produto que custava R${}, na promoção com desconto de {:.0f}% vai custar R${:.2f}'.format(preco, desconto*100, valor))