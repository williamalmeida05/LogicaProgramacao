#Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

quantidade = int(input('Quantidade de números: '))
count = 0
numeros = []

while(quantidade > count):
    numero =int(input(f'insira o numero{count + 1} de {quantidade}'))
    if numero > 0 and numero < 1000:
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

print(f'menor {menor}')
print(f'maior {maior}')