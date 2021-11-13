#Exercício Python 55: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
pesos = []
maior = 0
menor = 0
for c in range (0,5,1):
    pesos.append (float(input('Digite o peso da {}ª pessoa: '.format(c + 1))))
    if c == 0:
        maior = pesos[0]
        menor = pesos[0]
    else:
        if maior < pesos[c]:
            maior = pesos[c]
        if menor > pesos[c]:
            menor = pesos[c]    
print (pesos)
print ('O menor peso é {} e o maior é {}'.format(menor, maior))
