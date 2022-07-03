#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média
p1 = float(input("Digite a nota da P1: "))
p2 = float(input("Digite a nota da P2: "))
m = (p1+p2)/2
print('A nota da P1 foi {:.2f}, a da P2 foi {:.2f}, sendo assim a média desse aluno foi de {:.2f}'.format(p1,p2,m))