# Exercício Python 48: Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.
s = 0
cont = 0
for n in range(1,501,2):
    if n % 3 == 0:
        cont = cont + 1 
        s = (s + n)
print ('O somátório de todos os {} numeros no intervalo é {}'.format(cont, s))
