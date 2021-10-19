# Programa que faz a leitura de duas notas, calcula e mostra a média.

n1 = float (input ('Digite primeira nota: '))
n2 = float (input ('Digite segunda  nota: '))
m = ((n1+n2)/2)
print ('A média entre {} e {} é: {:.1f}' .format(n1,n2,m))