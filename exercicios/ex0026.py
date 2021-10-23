#Exercício Python 26: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes
#aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input('Digite uma frase: ')).strip()
fraseup = (frase.upper())
print (('A frase possui {} letras A sendo a primeira ocorrencia na posição {} e a ultima na posição {}').format(fraseup.count('A'), fraseup.find('A'), fraseup.rfind('A')))