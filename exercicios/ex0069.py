#Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.


print('-'*30)
de_maior = novinhas = homens = 0
while True:
    idade = 0
    while idade not in range(1,200):
        idade = int(input('Digite sua idade: '))
    if idade > 18:
        de_maior += 1
    sexo = str(input('Qual o seu sexo? [M/F]: ')).strip() .upper() [0]
    if sexo == 'F' and idade < 20:
        novinhas += 1
    if sexo == 'M':
        homens += 1
    encerrar = str(input('Deseja encerrar o programa? [Y/N]')).strip() .upper() [0]
    if encerrar == 'Y':
        break
print (f'Temos {de_maior} pessoas com mais de 18 anos.')
print (f'Temos {novinhas} mulheres com menos de 20 anos.')
print (f'{homens} homens foram cadastrados')
print ('FIM')
print ('-'*30)