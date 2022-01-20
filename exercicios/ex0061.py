#Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da PA: '))
enesimo_termo = 10
while enesimo_termo != 0:
    if enesimo_termo == 10:
        print (('{}'.format(primeiro_termo)), end=(' -> '))
        enesimo_termo -= 1
    elif enesimo_termo != 10:
        primeiro_termo += razao
        enesimo_termo -= 1
        print (('{}'.format(primeiro_termo)), end=(' -> '))
print('FIM')