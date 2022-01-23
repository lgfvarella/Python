#Exercício Python 63: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo: 0 – 1 – 1 – 2 – 3 – 5 – 8

numero = int(input('Digite a quantidade de elementos: '))
elementos = []
contador = 0
x = 1
y = 1
while contador != numero:
    if contador == 0:
        contador += 1
        elementos.append (x)
    elif contador == 1:
        contador += 1
        elementos.append (y)
    elif contador >= 2:
        if contador % 2 == 0:
            x = (x + y)
            contador += 1
            elementos.append (x)
        elif contador % 2 != 0:
            y = (x + y)
            contador += 1
            elementos.append(y)        
print(elementos)