# Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

vcasa = float (input ('Digite o valor do imóvel: R$ '))
renda = float (input ('Digite sua renda: R$ '))
tempof = int (input ('Digite em anos o tempo do financiamento: '))

prestacao = float (vcasa / (tempof*12))
if prestacao > (renda * .3):
    print ('Financiamento Negado')
else:
    print('Financiamento Aprovado com {} prestações no valor de R$ {:.2f}'.format((tempof*12), prestacao))