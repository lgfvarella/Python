#Exercício Python 72: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

numeros = ('zero','um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
numero_solicitado = -1
while True:
    if numero_solicitado not in range (0,21):
        numero_solicitado = int(input('Digite um número entre 0 e 20: '))
    else:
        print('Você digitou o número {}'.format(numeros [numero_solicitado]))
        break
print('FIM')