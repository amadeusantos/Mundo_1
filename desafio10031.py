km = int(input('Qual a distância da viagem em Km: '))
# valor = km * 0.5 if km <= 200 else km * 0.45
if km <= 200:
    valor = km * 0.5
else:
    valor = km * 0.45
print(f'O valor da viagem será de R${valor:.2f}.')
