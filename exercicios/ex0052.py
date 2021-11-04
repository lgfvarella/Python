#Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

num = int(input('Digite um número: '))
cont2 = 0
for c in range (1,num + 1):
    if num % c == 0:
        cont2 += 1
if cont2 > 2:
    print ('O número {} NÃO é um número primo'.format(num))
else:
    print ('SIM, o número {} é um número primo'.format(num))
