#Escreva um programa que converta uma temperatura digitada em Celsius para Fahrenheit e Kelvin
temperatura = float(input('Digite a temperatura em °C: '))
F = (temperatura * 1.8) + 32
K = temperatura + 273
print('A temperatura de {}°C corresponde a {}°F e {}K'.format(temperatura, F, K))