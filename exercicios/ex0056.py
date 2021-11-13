#Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
# No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
from datetime import datetime
data = datetime.now()
nomes = []
idade = []
sexo = []
media = 0
hvelho = 0
ihvelho = 0
mulheres = 0
ano = 0

for c in range (0,4,1):
    nomes.append(input('Digite seu nome:').strip().title())
    ano = (int(input('Digite sua data de nascimento: ')))
    idade.append (int(data.year - ano))
    media += idade[c]/4
    print('Digite M ou F para confirmar seu sexo')
    sexo.append(input('Digite seu sexo: ').strip().upper())
    print(sexo)
    if sexo [c] == ('M') and idade [c] > ihvelho:
        ihvelho = idade [c]
        hvelho = nomes[c]
    elif sexo [c] == ('F') and idade [c] < 20:
        mulheres += 1
print ('A média de idade do grupo é de {} anos, {} é o homem mais velho e temos {} mulheres abaixo de 20 anos de idade'.format(media, hvelho, mulheres))