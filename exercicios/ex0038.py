# Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:

n1 = int (input('Digite primeiro numero: '))
n2 = int (input('Digite segundo número: '))

if n1 > n2:
    print('O \033[01;34;40mPRIMEIRO\033[m valor é maior')
elif n1 < n2:
    print('O \033[01;34;40mSEGUNDO\033[m valor é maior')
else:
    print('Não existe maior, os valores são \033[01;31;40mIGUAIS\033[m')