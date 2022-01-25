#Exercício Python 67: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.

print('=-='*25)
while True:
    contador = 0
    numero = int(input('Digite um número negativo para SAIR ou positivo para ver sua tabuada:'))
    if numero < 0:
        break
    while contador != 10:
        print(f'{numero} x {contador} = {(numero*contador)}')
        contador += 1
    print('=-='*25)
print('FIM')