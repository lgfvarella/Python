#Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import datetime
lista = []
hoje = datetime.now()
maiores_de_idade = 0
menores_de_idade = 0
for c in range (1,8,1):
    lista.append (int (input('Digite seu ano de nascimento da {}ª pessoa: '.format(c))))
    print('Essa pessoa nasceu em {} e hoje {} tem anos'.format (lista[c - 1], (hoje.year - lista [c - 1])))
for x in lista:
    if (hoje.year - x) >= 18:
        maiores_de_idade += 1
    else:
        menores_de_idade += 1
print('temos {} pessoas menores de idade e {} maiores de idade'.format (menores_de_idade, maiores_de_idade))
    