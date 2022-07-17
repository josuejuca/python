# Faça um programa que leia a largura e a altura de uma parede em metros. Calcule a sua área e a quantidade de tinta necessária para pintá-la.
# Sabendo que cada litro de tinta,pinta uma área de 2m².
larg = float(input('Largura da parede: ')) # Vai receber a largura
alt = float(input('Altura da parede: ')) # Vai receber a altura
area = larg * alt  # Vai calcular a area
print('Sua parede tem a dimensão de {} x {} e sua área é de {}m².' .format(larg, alt, area)) # Vai mostrar a area
tinta = area / 2 # Vai calcular a quantidade de tinta 
print('Para pintar essa parede, você precisará de {}l de tinta.' .format(tinta)) # Vai mostrar a quantidade de tinta