#Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint
contador = 0
print('-'*30)
print('Olá!! Sou seu computador!! Vamos jogar PAR ou IMPAR!!')
print('-'*30)
while True:
    numero_jogador = int(input('Escolha um número: '))
    numero_pc = (randint(0,10))
    escolha_jogador =(str(input('Você quer par ou impar? [P/I]'))).upper() .strip() [0]
    soma = numero_jogador + numero_pc
    if soma % 2 == 0:
        resultado = 'Par'
    else:
        resultado = 'Impar'
    if resultado [0] == escolha_jogador:
        contador +=1 
        print(f'A soma entre os numeros escolhidos foi {soma}. Esse é um número {resultado}')
        print(f'Você ganhou!!')
    else:
        print(f'A soma entre os numeros escolhidos foi {soma}. Esse é um número {resultado}')
        print(f'Você perdeu após {contador} vitórias consecutivas!!')
        break
print('FIM')