#Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da
# turma varia entre 0 e 25, 26 e 60 e maior que 60; e então, dizer se a turma é
# jovem, adulta ou idosa, conforme a média calculada.

quantidade = int(input('Informe quantia de pessoas: '))
count = 0
idades = []
soma = 0

while (quantidade > count):
    idade = int(input(f' insira a idade {count + 1} de {quantidade}: '))
    if idade >= 0:
        idades.append(idade)
        count += 1
    else:
        print('idade invalida, insira novamente')

for idade in idades:
    soma = soma + idade
media = soma / quantidade
print(f'a média de idade é: {media}')

if media > 0 and media < 25:
    print('jovem')
elif media > 25 and media <= 60:
    print('adulto')
else:
    print('idoso')