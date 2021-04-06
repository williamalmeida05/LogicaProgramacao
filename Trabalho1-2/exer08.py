#Faça um programa que calcule o mostre a média aritmética de N notas.

quantidade = int(input('Quantidade de notas: '))
count = 0
notas = []

while (quantidade > count):
    nota = int(input(f' insira a nota {count + 1 } de {quantidade}'))
    if nota >= 0:
        notas.append(nota)
        count += 1
    else:
        print('invalido, favor inserir novamente')

soma = 0
for nota in notas:
    soma = soma + nota

media = soma / quantidade
print(f'a media é {media}')