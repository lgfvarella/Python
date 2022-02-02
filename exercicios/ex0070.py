#Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre: A) qual é o total gasto na compra. B) quantos produtos custam mais de R$1000. C) qual é o nome do produto mais barato.

soma = contador = prod_sup_mil = valor_produto_mais_barato = 0
produto_barato = ' '
while True:
    encerrar = ' '
    produto = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o valor do produto: '))
    soma += preco
    contador += 1
    if preco > 1000:
        prod_sup_mil += 1
    if contador == 1 or preco < valor_produto_mais_barato :
        produto_barato = produto
        valor_produto_mais_barato = preco
    while encerrar not in 'YN':
        encerrar = str (input('Deseja encerrar a compra? [Y/N]')).strip() .upper() [0]
    if encerrar == 'Y':
        break
print(f'O valor total da compra é {soma} o produto mais barato é o/a {produto_barato} e foram registrados {prod_sup_mil} produtos acima de 1000 reais.')