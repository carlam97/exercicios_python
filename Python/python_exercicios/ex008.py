#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milimetros 
metros = float(input('Digite o valor em metros: '))
cm = metros * 100
mm = metros * 1000
print('{} metros equivale a {} centimetros(cm) e {} milimetros(mm)'.format(metros, cm, mm))