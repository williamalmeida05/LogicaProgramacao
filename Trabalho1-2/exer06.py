#Altere o programa de cálculo dos números primos, informando,
# caso o número não seja primo, por quais número ele é divisível.

num = int(input('Digite um numero inteiro para saber se é primo: '))
count = 0
div = []

for i in range(num):
    if num % (i + 1 ) == 0:
        count += 1
        div.append(i + 1)
    else:
        count

if count == 2:
    print('O numero é primo divisivel por', div)

else:
    print(' O numero não é primo pois é divisivel por', div)
