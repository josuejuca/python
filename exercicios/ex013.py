# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento
salario = float(input('Qual é o valor do salário do funcionário? R$')) # Vai receber o salário
NovoSalario = salario + (salario * 15 / 100) # Vai aplicar o aumento
print('Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}' .format(salario, NovoSalario)) # Vai mostrar o resultado 