r1 = float(input('Digite o valor da primeira reta: '))
r2 = float(input('Digite o valor da segunda reta: '))
r3 = float(input('Digite o valor da terceira reta: '))
if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print(f'Com as retas {r1}, {r2} e {r3} é possível forma um triângulo.')
else:
    print(f'Com as retas {r1}, {r2} e {r3} não é possível forma um triângulo.')
