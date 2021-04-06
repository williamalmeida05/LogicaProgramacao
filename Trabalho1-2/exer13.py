#O Sr. Manoel Joaquim possui uma grande loja de artigos de R$ 1,99, com cerca de 10 caixas.
#Para agilizar o cálculo de quanto cada cliente deve pagar ele desenvolveu um tabela que contém o número de itens
#que o cliente comprou e ao lado o valor da conta. Desta forma a atendente do caixa precisa apenas contar quantos
#itens o cliente está levando e olhar na tabela de preços. Você foi contratado para desenvolver o programa que monta
#esta tabela de preços, que conterá os preços de 1 até 50 produtos, conforme o exemplo abaixo:
# Lojas Quase Dois -tabela de preços 1 - R$ 1.99 2 - R$ 3.98 ... 50 - R$ 99.50

produtos = int(input('digite a quantidade de produtos: '))
precos = []
n_produtos = 1
count = 0

while produtos > 50:
    produtos = int(input('digite a quantidade de produtos menos que 50:'))

for i in range(produtos):
    print(f'produto numero {n_produtos}')
    preco = precos.append(float(input('digite o preco do produto: ')))
    n_produtos += 1

for j in range(produtos):
    print(f'produto numero {n_produtos} = {precos [count]}')
    count += 1
    n_produtos += 1

