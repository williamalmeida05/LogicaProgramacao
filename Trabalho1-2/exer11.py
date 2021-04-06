#Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas
# e a quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos.

turmas = int(input('Numero de turmas: '))
alunos_turmas = []
turma = 1
soma = 0

for i in range(turmas):
    print(f'Turma: {turma}')
    alunos = int(input('Numero de alunos da turma: '))
    while alunos > 40:
        print(f'Turma {turma}, uma turma só pode ter 40 alunos ')
        alunos = int(input('Alunos da turma: '))
    turma += 1
    alunos_turmas.append(alunos)


for alunos in alunos_turmas:
    soma = soma + alunos

media2 = soma / len(alunos_turmas)
print(f'media2 {media2}')
