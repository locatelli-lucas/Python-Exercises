import math
catOp = float(input('Comprimento do cateto oposto: '))
catAd = float(input('Comprimento do cateto adjacente: '))

hip = math.hypot(catOp, catAd)

print("A hipotenusa vai medir {:.2f}".format(hip))