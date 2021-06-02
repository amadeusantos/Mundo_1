from math import tan, cos, sin, radians

ângulo = int(input('Qual o ângulo: '))
rad = radians(ângulo)
print(f'O valor do seno, do coseno e da tangente de {ângulo}º:')
print(f'Sen = {sin(rad):.2f} \nCos = {cos(rad):.2f} \nTang = {tan(rad):.2f}.')
