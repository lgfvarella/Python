#programa que lê um número Real qualquer pelo teclado e mostra na tela a sua porção Inteira.

from math import trunc

num = float (input ('Digite um numero real: '))
print ('o numero real {} tem como porção inteira {}'.format(num,trunc(num)))