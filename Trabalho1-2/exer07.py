#Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário.
# O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos.
# Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.

numero_para_range = int(input('Infore um número inteiro: '))
for numero in range(1, numero_para_range + 1):
    count = 0
    for j in range(1, numero +1):
        if numero % j == 0:
            count += 1
    print(f'{numero} É primo' if count == 2 else f'{numero} Não é primo.')
    print(f'realizou {numero + 1} divisões')