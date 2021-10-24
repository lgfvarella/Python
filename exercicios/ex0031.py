# Exercício Python 31: Desenvolva um programa que pergunte a distância de uma viagem em Km. 
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

distance = float (input ('Digite a distancia em kilometros a ser percorrida: '))
if distance < 200:
    print ('Sua viagem vai custar R$ {:.2f}'.format((distance*0.50)))
else:
    print ('Sua viagem vai custar R$ {:.2f}'.format((distance*0.45)))