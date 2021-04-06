#Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.
# Um número primo é aquele que é divisível somente por ele mesmo e por 1.

numero = int(input('Informe um numero: '))
count = 0
for i in range(1, numero + 1):
    if numero % i == 0:
        count += 1

print('é primo' if count == 2 else 'nao é primo')