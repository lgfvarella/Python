# Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe,
# de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, 
# se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

import datetime

datual = datetime.datetime.now()
ano = int (input('Digite seu ano de nascimento: '))
idade = (datual.year - ano)
if idade < 18:
    print ('Ainda faltam \033[1;34;40m{}\033[m anos para o alistamento'.format(18-idade))
    print ('Seu alistamento será em \033[1;34;40m{}\033[m'.format(datual.year + (18 - idade)))
elif idade >18:
    print ('Voce deveria ter se alistado há \033[1;31;40m{}\033[m anos'.format(idade-18))
    print ('Seu alistamento foi em \033[1;31;40m{}\033[m'.format(datual.year - (idade - 18)))
else:
    print ('Você nasceu em {} faz 18 anos em \033[1;35;40m{}\033[m'.format(ano, datual.year))
    print ('Você deve se alistar \033[1;35;40mIMEDIATAMENTE\033[m')
