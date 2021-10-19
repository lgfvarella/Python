import random
nome1 = input('Digite um nome: ')
nome2 = input('Digite um nome: ')
nome3 = input('Digite um nome: ')
nome4 = input('Digite um nome: ')

list = [nome1, nome2, nome3, nome4]
print('O sorteado para lavar a louça foi {}'.format(random.choice(list)))
