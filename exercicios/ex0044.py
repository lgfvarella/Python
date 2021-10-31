#Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto, 
# considerando o seu preço normal e condição de pagamento:
# à vista dinheiro/cheque: 10% de desconto
# à vista no cartão: 5% de desconto
# em até 2x no cartão: preço formal 
# 3x ou mais no cartão: 20% de juros

preco = float (input('Digite preço do produto: R$ '))
forma = int (input('Escolha a forma de pagamento: \n 1 - Dinheiro / Cheque \n 2 - 1 x Cartão \n 3 - 2 x no Cartão \n 4 - 3 ou + x no cartão \n Digite sua opção: '))
if forma == 1:
    print('O produto custa R$ {:.2f} e o desconto é de R$ {:.2f}, receber R$ {:.2f}'.format(preco, preco * 0.1, (preco - (preco * 0.1))))
elif forma == 2:
    print('O produto custa R$ {:.2f} e o desconto é de R$ {:.2f}, receber R$ {:.2f}'.format(preco, preco*0.05, preco - (preco*0.05)))
elif forma == 3:
    print('Receber R$ {:.2f}'.format(preco))
elif forma == 4:
    parcelas = int (input('Escolha quantidade de parcelas: '))
    print('Sua compra ficou no valor de {:.2f} com {:.2f} parcelas de {:.2f}'.format(preco + (preco * 0.2), parcelas,(preco + (preco * 0.2))/parcelas))