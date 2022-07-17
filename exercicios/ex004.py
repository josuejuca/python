# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possiveis sobre ele.
a = input('Digite algo: ')
print('O tipo primitivo desse valor é ', type(a)) #Sempre vai ser <class 'str'>
print('Só tem espaços? ', a.isspace()) # Ele consegue detectar ser só tem espaços
print('É um número? ', a.isnumeric()) # Ele consegue detectar se é um número 
print('É afalbetico? ', a.isalpha()) # Ele consegue detectar se é afalbetico "apenas letras"
print('É alfanumérico? ', a.isalnum()) # Ele consegue detectar se é afalnumérico
print('Está em letra maiúscula? ', a.isupper()) # Testa se está em letra maiúscula
print('Está em letra minúscula? ', a.islower()) # Testa se está em letra minúscula
print('Está capitalizada? ', a.istitle()) # Testa se está em letra maiúscula e letra minúscula
