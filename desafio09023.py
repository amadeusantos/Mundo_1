n = int(input('Digite um número entre 0 e 9999: '))
um = n // 1000
c = n % 1000 // 100
d = n % 100 // 10
i = n % 10
print(f'unidades: {i};')
print(f'dezenas: {d};')
print(f'Centenas: {c};')
print(f'Unidades de milhar: {um}.')
