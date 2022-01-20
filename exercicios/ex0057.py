#Exercício Python 57: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.

from pickle import FALSE, TRUE


nome = str(input ('Digite seu nome: ')).capitalize() .strip()
sexo = str(input('Digite seu sexo: ')).upper() [0] .strip()
flagsexo = FALSE
while flagsexo == FALSE:
    if sexo == 'M' or sexo == 'F':
        flagsexo = TRUE 
    else:
        print ('O campo sexo inserir somente M ou F')
        print('Po favor digite novamente!!')
        sexo = str(input('Digite seu sexo: ')).upper() .strip()   
print('Ok!!{} seu sexo é {} e o seu cadastro foi finalizado corretamente' .format(nome,sexo))