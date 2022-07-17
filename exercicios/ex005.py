# Faça um programa que receba um número inteiro e mostre na tela seu sucessor e seu antecessor.
n = int(input('Digite um número: ')) # Vai ler um número 
a = n - 1 # O número que vem antes 
s = n + 1 # O número que vem depois 
print('Analisando o valor {}, seu antecessor é {} e seu sucessor é {}.'.format( n, a, s))
# Outra opção
n1 = int(input('Digite um número: ')) # Vai ler um número 
print('Analisando o valor {}, seu antecessor é {} e seu sucessor é {}.'.format(n1, (n1-1),(n1+1)))
