# Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
#============ Legenda ===============
# n = numero de termos
# sn = somatório de termos
# n1 = primeiro termo
# en = enésimo termo
# razao = razao

n1 = (int (input ('Digite o valor do primeiro termo: ')))
razao = (int (input ('Digite a razão da PA: ')))
en = int (input('Digite quantos termos tem a PA:  '))
for c in range (n1,((n1+(en-1)*razao)+razao),razao):
    print(('{}'.format(c)), end=(' -> '))
print('FIM')