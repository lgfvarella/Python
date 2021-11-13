#Exercício Python 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:
frase = str(input('Digite sua palavra ou frase: ')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = ''
for c in range (len(junto)-1,-1,-1):
    inverso += (junto[c])
print('A frase digitada foi: \033[1;34;40m{}\033[m e o inverso dela é : \033[1;31;40m{}\033[m'.format(frase, inverso))
if junto == inverso:
    print('Temos um palindromo')
else:
    print('As frases não formam um palíndromo')