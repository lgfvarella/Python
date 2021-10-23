# usando Se 'if' e Senão 'else'
tempo = int (input('Digite quantos anos tem o seu veiculo: '))
if tempo <=3:
    print('Seu carro ainda é novo')
else:
    print('Seu carro é velho')

# programa que faz leitura do nome e fala se é bonito ou não

nome = str (input('Digite o seu nome completo: ')).strip() .title()
separado = (nome.split())
if ('Varella' in nome):
    print ('Que nome lindo você tem!')
print ('Seja bem vindo! {}'.format(separado[0]))

# Programa que faz a leitura de notas e calcula a média

n1 = float (input('Digite sua primeira nota: '))
n2 = float (input('Digite sua segunda nota: '))
m = (n1+n2)/2
if m>=6:
    print('Sua média foi {:.2f} Parabéns!'.format(m))
else:
    print('Sua média foi {:.2f} Está ruim! Estude mais!'.format(m))
