# Programa que  faz a leitura de um valor em metros e exibe a conversão em centímetros e milímetros
n1 = float (input (' Digite uma distancia em metros: '))
km = n1/1000
hm = n1/100
dam = n1/10
dm = n1*10
cm = n1*100
mm = n1*1000
print ('O valor de {} m é: \n em Kilometros {}km \n em Hectometros {}hm \n em decametros {} dam'.format(n1,km,hm,dam))
print ( ' em decimetros {} dm \n em centímetros {} cm \n em milimetros é {} mm'.format (dm,cm,mm))