from math import radians, sin, cos, tan
ang = float(input('Digite o ângulo que você deseja: '))
sen = sin(radians(ang))
co = cos(radians(ang))
ta = tan(radians(ang))

print('O ângulo de {}° tem o SEN de {:.2f}'.format(ang, sen))
print('O ângulo de {}° tem o COS de {:.2f}'.format(ang, co))
print('O ângulo de {}° tem a TAN de {:.2f}'.format(ang, ta))