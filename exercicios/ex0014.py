#programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

gc = float(input('Digite a temperatura em °C: ' ))
gf = float(gc*1.8+32)
print ('{}°C é equivalente a {:.2f}°F'.format((gc),(gf)))
