velocidade = int(input("Qual a velocidade atual do carro? "))

valorMulta = (velocidade - 80)*7

if velocidade > 80:
    print("\33[1;4;31mMULTADO! Você excedeu o limite permitido que é de 80Km/h")
    print("Você deve pagar uma multa de R${:.2f}!".format(valorMulta))
else:
    print("\33[33mTenha um bom dia! Dirija com segurança!")