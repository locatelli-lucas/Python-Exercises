largura = float(input("Largura da parede: "))
altura = float(input("Altura da parede: "))

areaParede = largura * altura
tinta = 0.5 * areaParede

print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².'.format(largura, altura, areaParede))
print('Para pintar essa parede, você precisará de {}l de tinta.'.format(tinta))
