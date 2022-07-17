# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média.
n1 = float(input('Primeira nota do aluno: ')) # Vai receber a primeira nota do aluno
n2 = float(input('Segunda nota do aluno: ')) # Vai receber a segunda nota do aluno
m = (n1 + n2) / 2 # Vai calcular a média
print('A média entre {:.1f} e {:.1f} é igual a {:.1f}' .format(n1, n2, m)) # Vai mostrar a média
# :.1f que dizer que depois do ponto flutuante coloque apenas 1 digito