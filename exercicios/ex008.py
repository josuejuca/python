# Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.
medida = float(input('Uma distância em metros: ')) # Vai receber medida em metros 
cm = medida * 100 # Vai converter em cm
mm = medida * 1000 # Vai converter em mm
print('A media de {}m corresponde a {:.0f}cm e {:.0f}mm'.format(medida,cm,mm)) # Vai mostrar o resultado.