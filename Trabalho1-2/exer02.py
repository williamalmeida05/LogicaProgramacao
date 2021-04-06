#Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.

quantidade = int(input('Quantidade de números: '))
count = 0
numeros = []

while(quantidade > count):
    numero =int(input(f'insira o numero{count + 1} de {quantidade}'))
    if numero and numero :
        numeros.append(numero)
        count += 1
    else:
        print('numero invalido, favor inserir novamente: ')
menor = numeros[0]
for i in numeros:
    if i < menor:
        menor = i

maior =numeros[0]
for i in numeros:
    if i > maior:
        maior = i
soma = maior + menor

print(f'menor {menor}')
print(f'maior {maior}')
print(f'a soma de {maior} + {menor} é {soma} ')