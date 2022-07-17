# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
preco = float(input('Qual é o preço do produto? R$')) # Vai receber o Preço
desc = preco * 5/100 # Vai calcular o desconto 
valor = preco - desc # Vai aplicar o desconto
print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}' .format(preco,valor)) # Vai mostrar o resultado 
# Outra opção
preco2 = float(input('\nQual é o preço do produto? R$')) # Vai receber o Preço
novoPreco = preco2 - (preco * 5 / 100) # Vai aplicar o desconto
print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}' .format(preco2,novoPreco)) # Vai mostrar o resultado 
