from datetime import date
nascimento = int(input('Ano de nascimento: '))
idade = date.today().year - nascimento
if 0 < idade < 5:
    print('Não tem idade para treinar!!!')
elif 5 <= idade <= 9:
    print('''O atleta tem {} anos
Classificação: \33[34mMIRIM'''.format(idade))
elif 10 <= idade <= 14:
    print('''O atleta tem {} anos
Classificação: \33[34mINFANTIL'''.format(idade))
elif 15 <= idade <= 19:
    print('''O atleta tem {} anos
Classificação: \33[34mJUNIOR'''.format(idade))
else:
    print('''O atleta tem {} anos
Classificação: \33[34mSÊNIOR'''.format(idade))