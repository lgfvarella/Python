#Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.

from random import randrange
from time import sleep

print('=-='*20)
print('''ESCOLHA UMA OPÇÃO
[0] - "PEDRA"
[1] - "PAPEL"
[2] - "TESOURA" ''')
lista = ['PEDRA', 'PAPEL', 'TESOURA']
x = int(input('Digite sua opção: '))
if (x < 0 or x > 2):
    print ('Você não escolheu corretamente, tente novamente!')
else:
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO')
    print ('=-='*20)
    print ('JOGADOR ESCOLHEU: {}'.format(lista[x]))
    y = randrange(0,3)
    print ('COMPUTADOR ESCOLHEU: {}'.format(lista[y]))
    print ('=-='*20)
    if x == y:
        print('\033[1;37;40mEMPATE')
    elif (x == 0 and y == 1) or (x==1 and y==2) or (x == 2 and y == 0):
        print ('\033[1;31;40mCOMPUTADOR VENCEU!!')
    elif (x == 1 and y == 0) or (x==2 and y==1) or (x == 0 and y == 2):
        print ('\033[1;34;40mJOGADOR VENCEU!!')
    