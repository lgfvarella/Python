#algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float (input ('Digite o salário atual: R$'))
ajuste = (salario*15/100)
print ('O salário atual é {} com o reajuste o salário passará a ser {:.2f}'.format ((salario),(salario+ajuste)))