nome = input("Digite seu nome: ").strip().split()
print('Muito prazer em te conhecer!')
print("Seu primeiro nome é {}".format(nome[0]))
print("Seu último nome é {}".format(nome[nome.__len__()-1]))