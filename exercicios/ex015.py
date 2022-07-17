# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por km rodado.
dias = int(input('Quantos dias alugados? ')) # Vai receber os dias 
km = float(input('Quantos Km rodados? ')) # Vai receber os km
pago = (dias * 60) + (km * 0.15) # Vai calcular o resultado 
print('O total a pagar é de R${:.2f}' .format(pago)) # Vai mostrar o resultado
