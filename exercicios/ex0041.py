# Exercício Python 041: A Confederação Nacional de Natação precisa de um programa 
# que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# Até 9 anos: MIRIM / Até 14 anos: INFANTIL / Até 19 anos: JÚNIOR / Até 25 anos: SÊNIOR
# Acima de 25 anos: MASTER

from time import localtime

#dia = int (input('Digite o dia do seu nascimento: '))
#mes = int (input('Digite o mês do seu nascimento: '))
nasc = int (input('Digite o ano do seu nascimento: '))
ano = (localtime()[0])
idade = (ano - nasc) 
if (idade) <= 9:
    print ('Quem nasceu em {} tem ou completará {} de idade portanto está classificado como MIRIM'.format(nasc, idade))
elif (idade) > 9 and (idade) <= 14:
    print ('Quem nasceu em {} tem ou completará {} de idade portanto está classificado como INFANTIL'.format(nasc, idade))
elif (idade) > 14 and (idade) <= 19:
    print ('Quem nasceu em {} tem ou completará {} de idade portanto está classificado como JUNIOR'.format(nasc, idade))
elif (idade) > 19 and (idade) <= 25:
    print ('Quem nasceu em {} tem ou completará {} de idade portanto está classificado como SÊNIOR'.format(nasc, idade))
else:
    print ('Quem nasceu em {} tem ou completará {} de idade portanto está classificado como MASTER'.format(nasc, idade))
