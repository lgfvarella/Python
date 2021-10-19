#algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

p = float (input ('Digite preço do produto: '))
print ('O valor final do produto é: {:.2f}'.format(p-(p*0.05)))