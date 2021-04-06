#Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

numero = int(input('informe um numero inteiro que deseja calcular o fatorial '))
fatorial = numero
for count in range(numero - 1, 0, -1):
    fatorial = fatorial * count

print(fatorial)