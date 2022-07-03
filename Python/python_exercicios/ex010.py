#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
din = float(input('Quanto dinheiro você tem na carteira? R$'))
conv = din / 5.13
print('Com R${:.2f} atualmente você pode comprar US${:.2f}'.format(din, conv))
 