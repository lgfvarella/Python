#Exercício Python 62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

from pickle import FALSE, TRUE


primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da PA: '))
total_termos = int(input('Quantos termos tem a PA: '))
sair = FALSE
contador = 1
while sair == FALSE:
    if contador == 1:
        print(('{}'.format(primeiro_termo)), end=(' -> '))
        contador += 1
    elif contador > 1 and contador < total_termos:
        primeiro_termo += razao
        print(('{}'.format(primeiro_termo)), end=(' -> '))
        contador += 1
    elif contador == total_termos:
        primeiro_termo += razao
        print(('{}').format (primeiro_termo))
        adicao_de_termos = int(input(print('''DIGITE [ 0 ] PARA SAIR ou a quantidade de termos a ser adicionada!: ''')))
        if  adicao_de_termos != 0:
            total_termos += (adicao_de_termos -1)
        else:
            sair = TRUE
print('FIM')
