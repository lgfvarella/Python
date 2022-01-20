# Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. 
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint
from time import sleep
numeropc = randint (0,10)
tentativas = 0
print('Ei!!')
sleep(2)
print('Você ai!!')
sleep(2)
print('Sou seu computador!!! Bora jogar!! estou pensando em um número de 0 a 10 tente adivinhar!!')
sleep(2)
acertou = False
while not acertou:
    numerogamer = int(input('Qual é o seu palpite?: '))
    tentativas +=  1
    if numerogamer < numeropc:
        print ('Maior')
    elif numerogamer > numeropc:
        print ('Menor')
    elif numerogamer == numeropc:
        acertou = True
print ('Parabéns!! você acertou após {} tentativas'.format(tentativas))