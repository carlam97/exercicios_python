#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento
nome = str(input('Digite o nome do funcionário: '))
salario = float(input('Digite o valor do salário atual: R$'))
aumento = int(input('Digite o valor de aumento em porcentagem(%) '))
div = salario * (aumento / 100)
novo = salario + div
print('{} recebe um salário de R${:.2f}, com o aumento de {}% seu novo salário será de R${:.2f}'.format(nome, salario, aumento, novo))
