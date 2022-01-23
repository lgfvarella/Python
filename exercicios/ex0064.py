#Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
print('=-='*10)
numero = soma = contador = 0
numero = int(input('Digite um número a ser somado [999 para SAIR] '))
while numero != 999:
    soma += numero
    contador += 1
    numero = int(input('Digite um número a ser somado [999 para SAIR] '))
print('{} números foram digitados e a soma dos numeros digitados é: {}'.format(contador,soma))
print('=-='*10)
    