# Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, 
# mostrando uma mensagem no final, de acordo com a média atingida:
# – Média abaixo de 5.0: REPROVADO
# – Média entre 5.0 e 6.9: RECUPERAÇÃO
# – Média 7.0 ou superior: APROVADO

n1 = float (input('Digite a primeira nota: '))
n2 = float (input('Digite a segunda nota: '))
m = ((n1 + n2)/2)
print ('A média do aluno foi {}'.format(m))
if m < 5:
    print ('Aluno \033[1;31;40mREPROVADO')
elif m >= 5 and m < 7:
    print ('Aluno em \033[1;37;40mRECUPERAÇÃO')
elif m >= 7:
    print ('Aluno \033[1;34;40mAPROVADO')