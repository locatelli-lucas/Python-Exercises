nome = input('Digite seu nome: ').strip()

primeiroNome = nome.split()[0]
split = primeiroNome.__len__()
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome completo tem {} letras'.format(nome.__len__()-nome.count(' ')))
print('Seu primeiro nome é {} e ele tem {} letras'.format(primeiroNome, split))

