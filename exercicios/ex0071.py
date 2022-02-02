#Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS: considere que o caixa possui cédulas de R$50, R$20, R$10, R$5 e R$2.
saque50 = saque20 = saque10 = saque5 = saque2 = 0
print('='*30)
print('{:^30}'.format('VARELLA BANKING'))
print('='*30)
valor_saque = int(input('Digite o valor do saque: R$  '))
while True:
    if valor_saque >= 50:
        valor_saque -= 50
        saque50 += 1
    elif valor_saque < 50 and valor_saque >= 20:
        valor_saque -=20
        saque20 += 1
    elif valor_saque < 20 and valor_saque >= 10:
        valor_saque -= 10
        saque10 += 1
    elif valor_saque < 10 and valor_saque >= 5:
        valor_saque -= 5
        saque5 += 1
    elif valor_saque < 5 and valor_saque >= 2:
        valor_saque -=2
        saque2 += 1
    elif valor_saque <= 0:
        break
print('='*30)
if saque50 != 0:
    print(f'Total de {saque50} cedula(s) de R$50')
if saque20 != 0:
    print(f'Total de {saque20} cédula(s) de R$20')
if saque10 !=0:
    print(f'Total de {saque10} cédula(s) de R$10')
if saque5 !=0:
    print(f'Total de {saque5} cédula(s) de 5')
if saque2 != 0:
    print(f'Total de {saque2} cédula(s) de 2')
print('='*30) 

        

