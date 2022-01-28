#Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.


print('-'*30)
de_maior = novinhas = homens = 0
while True:
    idade = 0
    sexo = encerrar = ' '
    while idade not in range(1,200):
        idade = int(input('Digite sua idade: '))
    if idade > 18:
        de_maior += 1
    while sexo not in ('MmFf'):
        sexo = str(input('Qual o seu sexo? [M/F]: ')).strip() .upper() [0]
    if sexo == 'F' and idade < 20:
        novinhas += 1
    if sexo == 'M':
        homens += 1
    while encerrar not in ('YyNn'):
        encerrar = str(input('Deseja encerrar o programa? [Y/N]')).strip() .upper() [0]
    if encerrar == 'Y':
        break
print (f'Temos \033[01;34;40m{de_maior}\033[m pessoa(s) com mais de 18 anos.')
print (f'Temos \033[01;34;40m{novinhas}\033[m mulher(es) com menos de 20 anos.')
print (f'\033[01;34;40m{homens}\033[m homem(s) foram cadastrados')
print ('FIM')
print ('-'*30)