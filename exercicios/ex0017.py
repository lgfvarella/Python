#Programa que lê o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. 
#Calcule e mostre o comprimento da hipotenusa.

import math
co = float(input('Digite comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
#hipot = (((co**2)+(ca**2))**(1/2))
hipot = math.hypot(co,ca)
print('Sendo o cateto oposto {} e o cateto adjacente {} a hipotenusa será {:.2f}'.format(co,ca,hipot))
