# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
n = int(input('Digite um número: ')) # Vai receber n
d = n * 2 # O dobro de n
t = n * 3 # O triplo de n
r = n ** (1/2) # A raiz quadrada de n
print('O dobro de {} vale {}.'.format(n,d)) # Vai mostra o dobro de n
print('O triplo de {} vale {}.'.format(n,t)) # Vai mostra o triplo de n
print('A raiz quadrada de {} vale {:.2f}.\n'.format(n,r)) # Vai mostra a raiz quadrada de n
# Outra opção
n1 = int(input('Digite um número: ')) # Vai receber n1
print('O dobro de {} vale {}.'.format(n1, (n1*2))) # Vai mostra o dobro de n1
print('O triplo de {} vale {}.'.format(n1,(n1*3))) # Vai mostra o triplo de n1
print('A raiz quadrada de {} vale {:.2f}.'.format(n1, pow(n1, (1/2)) )) # Vai mostra a raiz quadrada de n1
