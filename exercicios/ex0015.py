#programa que pergunta a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
#Calcula o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

dia = int (input('Quantos dias o carro ficou alugado? '))
km = float (input('Quantos km o carro percorreu? '))
print ('{} dias de locação e {} km percorridos custam R${:.2f}'.format((dia),(km),((dia*60)+(km*0.15))))
