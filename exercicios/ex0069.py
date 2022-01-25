#Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

print('-'*30)
idade = -1
contador_maior_de_idade = 0
contador_mulheres_de_menor = 0
contador_homens = 0
sexo = ' '
while True:
    while idade not in range(0,200):
        idade = int(input('Digite sua Idade: '))
        if idade > 18:
            contador_maior_de_idade += 1
        while sexo not in ('MmFf'):
            sexo = str(input('Digite seu sexo [M/F]: ')).strip() .upper() [0]    
            if idade < 20 and sexo == 'F':
                contador_mulheres_de_menor += 1
            if sexo == 'M':
                contador_homens += 1
        encerrar = str(input('Deseja encerrar o programa? [Y/N]')).strip() .upper() [0]
        if encerrar == 'Y':
                break
print(f'Temos {contador_maior_de_idade} pessoas maiores de 18 anos \nTemos {contador_homens} pessoas do sexo masculino e temos {contador_mulheres_de_menor} mulheres com menos de 20 anos')
print('FIM')
        
    