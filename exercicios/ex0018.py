# Programa que lê um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math
x = float (input('Digite um angulo: '))
sin = math.sin(math.radians (x))
cos = math.cos(math.radians(x))
tan = math.tan(math.radians(x))
print ('O angulo {} tem como seno {:.2f}, cosseno {:.2f} e tangente {:.2f}.'.format(x,sin,cos,tan))
