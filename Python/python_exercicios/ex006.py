#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada
valor = int(input('Digite um valor: '))
dobro = valor * 2
triplo = valor * 3
raiz = valor ** (1/2)
print('O dobro de {} é {}'.format(valor, dobro))
print('O triplo de {} é {}'.format(valor, triplo))
print('A raiz quadrada de {} é {}'.format(valor, raiz))

print('='*70)

valor = int(input('Digite um valor: '))
dobro = valor * 2
triplo = valor * 3
raiz = valor ** (1/2)
print('O dobro de {} é {}. \nO triplo de {} é {}. \nA raiz quadrada de {} é {:.2f}'.format(valor, dobro, valor, triplo, valor, raiz))