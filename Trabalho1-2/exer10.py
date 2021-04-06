#Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores.
# Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.

eleitores = int(input('Informe a quantidade de eleitores: '))
candidato1 = 0
candidato2 = 0
candidato3 = 0
votantes = 0

while (votantes < eleitores):
    voto = int(input('Clique 1 para votar no candidato1, 2 para o candidato2 e 3 para o candidato3: '))

    if (voto == 1):
        candidato1 = candidato1 + 1
        votantes = votantes + 1

    elif (voto == 2):
        candidato2 = candidato2 + 1
        votantes = votantes + 1

    elif (voto == 3):
        candidato3 = candidato3 + 1
        votantes = votantes + 1

    else:
        print('Voto invalido: ')

print(f'O candidato1 teve {candidato1} votos')
print(f'O candidato2 teve {candidato2} votos')
print(f'O candidato3 teve {candidato3} votos')