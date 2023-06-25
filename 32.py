from datetime import date
nascimento = int(input("Qual seu ano de nascimento jovem? "))
idade = date.today().year - nascimento

print('Quem nasceu em {} tem {} anos em {}'.format(nascimento, idade, date.today().year))

if idade > 18:
    print("Você já deveria ter se alistado há {} anos".format(idade - 18))
    print("Seu alistamento foi em {}".format(date.today().year - (idade - 18)))
elif idade == 17 and idade > 0:
    print("Ainda falta {} ano para seu alistamento".format(18 - idade))
    print("Seu alistamento será em {}".format(nascimento + 18))
elif idade == 18 and idade > 0:
    print("VOCÊ TEM QUE SE ALISTAR IMENDIATAMENTE")
elif idade < 18 and idade > 0:
    print("Ainda faltam {} anos para seu alistamento".format(18 - idade))
    print("Seu alistamento será em {}".format(nascimento + 18))

