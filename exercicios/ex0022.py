#Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas e minúsculas.
#Quantas letras ao todo (sem considerar espaços).
#Quantas letras tem o primeiro nome.

name = str (input('Digite o seu nome completo: ')) .strip()
print ('Seu nome em maiusculo: {}'.format(name.upper()))
print ('Seu nome em minusculo: {}'.format(name.lower()))
print ('Seu nome tem {} letras'.format(len(name) - name.count(' ')))
#print ('Seu primeiro nome tem {} letras'.format(name.find(' ')))
x = (name.split())
print ('Seu primeiro nome é {} e tem {} letras'.format (x[1], len(x[1])))