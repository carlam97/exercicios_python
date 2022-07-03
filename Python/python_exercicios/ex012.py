#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com o desconto estipulado
produto = str(input('Digite o nome do produto: '))
preco = float(input('Qual é o preço do produto? R$'))
desconto = int(input('Qual é o desconto oferecido?'))
desc = desconto / 100
novo = preco * (1 - desc)
print('O preço normal do(a) {} é de R${:.2f}, com o desconto oferecido de {}% o novo valor desse produto será de R${:.2f}'.format(produto, preco, desconto, novo))