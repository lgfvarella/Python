#Exercício Python 35: Desenvolva um programa que leia o comprimento de três retas 
# e diga ao usuário se elas podem ou não formar um triângulo.

a = float (input ('Digite o tamanho do primeiro lado: '))
b = float (input ('Digite o tamanho do segundo lado: '))
c = float (input ('Digite o tamanho do terceiro lado: '))
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print (maior)
if maior >= (((a + b + c) - maior)):
    print ('NAO, é possivel fazer um triangulo com essas medidas')
else:
    print ('SIM, é possivel fazer um triangulo com essas medidas')