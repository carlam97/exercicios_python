#Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor

num = int(input('Digite um número: '))
ant = (num - 1)
suc = (num + 1)
print('Analisando o número {}, seu antecessor é {} e o seu sucessor é {}'.format(num, ant, suc))

print('='*70)

num = int(input('Digite um valor: '))
print('Analisando o valor {}, seu antecessor é {} e o seu sucessor é {}'.format(num, num-1, num+1))