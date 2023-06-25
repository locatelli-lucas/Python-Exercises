distancia = int(input("Qual a distância da viagem em Km? "))

if distancia <= 200:
    valor = distancia*0.5
     
else:
    valor = distancia*0.45
    
print("O valor da sua viagem é de \33[1;36mR${:.2f}".format(valor))
