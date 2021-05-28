dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos quilômetros foram percorridos? '))
valor = (dias * 60) + (km * 0.15)
print(f'O valor dos {dias} dias e dos {km}km de uso do carro ficam R${valor:.2f}.')
