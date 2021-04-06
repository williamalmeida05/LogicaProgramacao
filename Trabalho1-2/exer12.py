#Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs
# e o valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.

quantidade_cds = int(input('Informe a quantidade de cd: '))
cds = []
numero_cd = 1

for i in range(quantidade_cds):
    print(f'Numero de CD: {numero_cd}')
    valor_cd = cds.append(float(input('Informe o valor do CD: ')))
    numero_cd += 1


media = sum(cds) / len(cds)
print(f'A media para cada CD é: {media}')