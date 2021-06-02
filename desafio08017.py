from math import sqrt, pow

co = float(input('Qual o valor do cateto oposto: '))
ca = float(input('Qual o valor do cateto adjacente: '))
hi = sqrt(pow(co, 2) + pow(ca, 2))  # hypot(co, ca)
print(f'O valor da hipotenusa é {hi:.2f}.')
