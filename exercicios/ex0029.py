# Exercício Python 29: Escreva um programa que leia a velocidade de um carro. 
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. 
# A multa vai custar R$7,00 por cada Km acima do limite.

veloc = float (input ('Velocidade detectada: '))
if veloc >80:
    multa = float ((veloc - 80)*7)
    print ('O limite da via é de 80km/h e você passou a {}Km/h e foi multado'.format(veloc))
    print ('O valor da multa é: R${:.2f}'.format(multa))
else:
    print ('Condutor dentro do limite de velocidade')
