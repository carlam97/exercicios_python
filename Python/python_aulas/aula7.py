nome = str(input('Qual é o seu nome?'))
print('Prazer, meu nome é',nome)

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
soma = n1 + n2
multi = n1 * n2
divisao = n1 / n2
divinteria = n1 // n2
expo = n1 ** n2
print('A soma é {}, o produto é {} e a divisão é {:.3f}'.format(soma, multi, divisao))
print('A divisão inteira é {} e a potência é {}'.format(divinteria, expo))