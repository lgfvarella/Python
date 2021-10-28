#  Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer 
#  e peça para o usuário escolher qual será a base de conversão:
#  1 para binário, 2 para octal e 3 para hexadecimal.
print ('-='*20)
num = int (input('Digite um número: '))
print ('-='*20)
print ('Agora escolha a base de conversão')
base = int (input('Escolha: \n 1 - binário \n 2 - octal \n 3 - hexadecimal \n -->>: '))
if base == 1:
    print (bin(num)[2:])
elif base == 2:
    print(oct(num)[2:])
elif base == 3:
    print(hex(num)[2:])
else:
    print('Opção inválida, tente novamente!')