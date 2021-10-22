#Manipulando Strings - tambem conhecido como manipulação de range.

# Obs: A contagem sempre vai ter o inicio em 0 'zero'. No exemplo abaixo a letra C da palavra Curso está ocupando o espaço 0.

frase = "Curso em Video Python"

# Ex1: Buscando somente uma letra da string
print ("Ex1: {}".format (frase[9]))

# Ex2: Buscando um conjunto de caracteres da string, neste caso pegamos do 9 ao 12 pois o 13 não é inserido na contagem.
print ("Ex2: {}".format (frase[9:13]))

# Ex3: Buscando um conjunto de caracteres da string, neste caso pegamos do 9 ao 20 pois o 21 não é inserido na contagem.
print ("Ex3: {}".format (frase[9:21]))

# Ex4: Buscando um conjunto de caracteres da string mas intercalando de dois em dois.
print ("Ex4: {}".format (frase[9:21:2]))

# Ex5: Buscando um conjunto de caracteres da string só que ao omitir o numero de inicio o python busca desde o inicio
print ("Ex5: {}".format (frase[:5]))

#Ex6: Buscando um conjunto de caracteres da string só que ao omitir o numero do fim o python vai fatiar a frase do 15 até o final
print("Ex6: {}".format(frase[15:]))

#Ex7: Buscando um conjunto de caracteres da string só que ao omitir o numero do meio o python vai fatiar começando
#pelo numero apontado no inicio e vai pular conforme o numero apontado no final
print ("Ex7: {}".format(frase[9::3]))

#Ex8: Faz a análise do comprimento da váriavel retornando a quantidade de caracteres.
print ("Ex8: {}".format(len (frase)))

#Ex9: Faz a contagem da quantidade do caracter referenciado nos caracteres da string. Obs: ele é case sensitive.
print ("Ex9: {}".format(frase.count("o"))) 

#Ex10: Faz a contagem da quantidade do caracter referenciado nos caracteres da string já fatiando a string. 
#Obs: ele é case sensitive.
print ("Ex10: {}".format(frase.count("o",0,13)))

# Ex11: Faz a localização de caracteres ou partes da string retornando o numero inicial da localização. 
# se o resultado encontrado for -1 quer dizer que essa procura nao foi localizada ou nao existe.
print ("Ex11: {}".format(frase.find('deo')))

#Ex12: Faz a verificacao de caracteres ou partes da string retornando TRUE or False
print ('Ex12: {}'.format('Curso' in frase))

#Ex13: Faz a troca de caracteres ou palavras da string pelas referenciadas.
print ('Ex13: {}'.format(frase.replace('Python','Android')))

#Ex14: Faz todos os caracteres ficarem maiusculos
print('Ex14: {}'.format(frase.upper()))

#Ex15: Faz todos os caracteres ficarem minusculos
print('Ex15: {}'.format(frase.lower()))

#Ex16: Faz somente o primeiro caracter da string ficar maiusculo.
print('Ex16: {}'.format(frase.capitalize()))

#Ex17: Faz com que todas as palavras da string fiquem com a primeira letra em maiusculo
print('Ex17: {}'.format(frase.title()))

frase2 = ('   Aprenda Python   ')

# Ex18: Faz com que os espaços existentes no inicio e no final da string sejam removidos.
print ('Ex18: {}'.format(frase2.strip()))

# Ex19: Faz com que os espaços existentes no final da string sejam removidos.
print ('Ex19: {}'.format(frase2.rstrip()))

# Ex20: Faz com que os espaços existentes no inicio da string sejam removidos.
print ('Ex20: {}'.format(frase2.lstrip()))

# Ex21: Faz com que a string se torne uma lista, dividindo a string em cada espaço existente nela. 
# Obs: professor comeca a explicar aos 28min do video
print ('Ex21: {}'.format(frase.split()))

list = ['Banana','Abacaxi','Morango']

#Ex22: Junta elementos de uma lista formando uma string
print ('Ex22: {}'.format('-'.join(list)))