#Exercício Python 24: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”

cidade = str(input('Digite o nome da cidade: ')).strip() .title()
x = (cidade.split())
print (x)
print ('Santo' in (x[0]))