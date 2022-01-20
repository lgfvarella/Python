#Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.

valor1 = float(input('Digite o primeiro valor: '))
valor2 = float(input('Digite o segundo valor: '))
print ('[ 1 ] somar \n[ 2 ] multiplicar \n[ 3 ] maior \n[ 4 ] novos números \n[ 5 ] sair do programa')
opcao = int(input(print('selecione uma opção: ')))
while opcao != 5:
    if opcao == 1:
        print ('{:.2f} + {:.2f} = {:.2f}'.format(valor1,valor2,(valor1+valor2)))
        print ('[ 1 ] somar \n[ 2 ] multiplicar \n[ 3 ] maior \n[ 4 ] novos números \n[ 5 ] sair do programa')
        opcao = int(input(print('selecione uma opção: ')))
    elif opcao == 2:
        print ('{:.2f} x {:.2f} = {:.2f}'.format(valor1,valor2,(valor1*valor2)))
        print ('[ 1 ] somar \n[ 2 ] multiplicar \n[ 3 ] maior \n[ 4 ] novos números \n[ 5 ] sair do programa')
        opcao = int(input(print('selecione uma opção: ')))
    elif opcao == 3:
        if valor1 > valor2:
            print('{:.2f} é maior que {:.2f}'. format(valor1,valor2))
            print ('[ 1 ] somar \n[ 2 ] multiplicar \n[ 3 ] maior \n[ 4 ] novos números \n[ 5 ] sair do programa')
            opcao = int(input(print('selecione uma opção: ')))
        elif valor2 > valor1:
            print('{:.2f} é maior que {:.2f}'.format(valor2,valor1))
            print ('[ 1 ] somar \n[ 2 ] multiplicar \n[ 3 ] maior \n[ 4 ] novos números \n[ 5 ] sair do programa')
            opcao = int(input(print('selecione uma opção: ')))
        elif valor1 == valor2:
            print('O valores são iguais')
            print ('[ 1 ] somar \n[ 2 ] multiplicar \n[ 3 ] maior \n[ 4 ] novos números \n[ 5 ] sair do programa')
            opcao = int(input(print('selecione uma opção: ')))
    elif opcao == 4:
        valor1 = float(input('Digite o primeiro valor: '))
        valor2 = float(input('Digite o segundo valor: '))
        print ('[ 1 ] somar \n[ 2 ] multiplicar \n[ 3 ] maior \n[ 4 ] novos números \n[ 5 ] sair do programa')
        opcao = int(input(print('selecione uma opção: ')))
    elif opcao < 1 or opcao > 5:
        print('Selecione uma opção válida')
        print ('[ 1 ] somar \n[ 2 ] multiplicar \n[ 3 ] maior \n[ 4 ] novos números \n[ 5 ] sair do programa')
        opcao = int(input(print('selecione uma opção: ')))