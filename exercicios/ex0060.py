#Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial. 
# Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120

fatorando = int(input('Digite o numero a ser fatorado:'))
fator = fatorando - 1
resultado = fatorando * fator 
while fator != 1:
    fator -= 1
    resultado = (resultado*fator)
print('O fatorial do {} é {}'.format(fatorando,resultado)) 