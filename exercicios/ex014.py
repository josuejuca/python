# Faça um programa que converta um temperatura digitada em °C e converta para °F
c = float(input('Informe a temperatura em °C: ')) # Vai receber a temperatura 
f = ( ( 9 * c ) / 5 ) + 32 # Vai transformar em °F
print('A temperatura de {}°C corresponde a {}°F!' .format(c, f)) # Vai mostrar o resultado