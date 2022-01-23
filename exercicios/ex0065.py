#Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

media = numero = menor = maior = int(input('Digite um número: '))
soma = contador = 0
continuar = str(input('Quer continuar? [Y/N]')).upper() [0]
while continuar == 'Y':
    soma += numero
    contador += 1
    media = (soma/contador)
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero
    numero = int(input('Digite um número: '))
    continuar = str(input('Quer continuar? [Y/N]')).upper() .strip() [0]
print('A média dos valores digitados é {}'.format(media))
print('O maior valor digitado foi {}'.format(maior))
print('O menor valor digitado foi {}'.format(menor))
    