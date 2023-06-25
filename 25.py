n = int(input("Digite um número qualquer: "))

if n % 2 == 0:
    print("O número {} é \33[4;33mPAR".format(n))
else:
    print("O número {} é \33[4;33mÍMPAR".format(n))