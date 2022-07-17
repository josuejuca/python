# Crie um programa que leia quanto dinheiro uma pessos tem na carteira e mostre quantos Dólares ela pode comprar.
# Considere US$1.00 = R$ 5.41
real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = real / 5.41
euro = real / 5.46
print('Com R${:.2f} você pode comprar US${:.2f}' .format(real,dolar))
print('Com R${:.2f} você pode comprar €{:.2f}' .format(real,euro))
