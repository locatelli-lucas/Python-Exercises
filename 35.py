peso = float(input('Qual seu peso? '))
altura = float(input("Qual sua altura? "))

IMC = peso / altura**2

if IMC < 18.5:  
    print("Seu IMC é de {:.1f} e você está \33[4;31mABAIXO DO PESO".format(IMC))
elif 18.5 <= IMC <= 25:
    print("Seu IMC é de {:.1f} e você está no \33[4;32mPESO IDEAL".format(IMC))
elif 25 < IMC <= 30:
    print("Seu IMC é de {:.1f} e você está com \33[4;33mSOBREPESO".format(IMC))
elif 30 < IMC <= 40:
    print("Seu IMC é de {:.1f} e você está \33[1;4;31mOBESO".format(IMC))
else:
    print("Seu IMC é de {:.1f} e você está com \33[1;4;37mOBESIDADE MÓRBIDA".format(IMC))