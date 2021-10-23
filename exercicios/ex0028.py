# Programa que faz o computador “pensar” em um número inteiro entre 0 e 5 e 
# Pede para o usuário tentar descobrir qual foi o número escolhido pelo computador. 
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random

numpc = int (random.randrange(0,6))
numan = int (input('Digite um numero de 0 a 5: '))
#if numan <0 or >5:
#    print('O número escolhido não está entre 0 e 5')
print('O numero escolhido por vc foi {} e o computador escolheu {}'.format(numan, numpc))
if numpc == numan:
    print('You Win! Congratulations!')
else:
    print('You Lose! Try Again!')