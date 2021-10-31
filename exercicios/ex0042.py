# Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# EQUILÁTERO: todos os lados iguais
# ISÓSCELES: dois lados iguais, um diferente
# ESCALENO: todos os lados diferentes

a = float (input ('Digite o tamanho do primeiro segmento: '))
b = float (input ('Digite o tamnho do segundo segmento: '))
c = float (input ('Digite o tamanho do terceiro segmento: '))
maior = a
if (b > a) and (b > c):
    maior = b
elif (c > a) and (c > b):
    maior = c
if maior < ((a + b + c)- maior):
    print('Sim, é possivel fazer um triangulo com esses segmentos.')
    if a == b and b == c and a == c:
        print('Com esses segmentos teremos um triangulo EQUILÁTERO')
    elif a != b and b != c and a != c:
        print ('Com esses segmentos teremos um triangulo ESCALENO')
    else:
        print ('Com esses segmentos teremos um triangulo ISOSCELES')
elif maior > ((a + b + c)- maior):
    print('Não é possivel fazer um triangulo com esses segmentos.')
