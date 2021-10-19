#Programa que faz a leitura da largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

rendimento = 2
w = float (input('Digite a largura da parede: '))
h = float (input('Digite a altura da parede: '))
print ('A área a ser pintada tem {:.2f} m2'.format(w*h))
print ('A quantidade de tinta necessária para o serviço é: {:.2f} L'.format((w*h)/rendimento))
