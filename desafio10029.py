v = float(input('Qual a velocidade do carro: '))
if v > 80:
    multa = (v - 80) * 7.0
    print(f'Devido a sua velocidade o senhor foi multado em R${multa:.2f}.')
print(f'Bom dia, dirija com cuidado!')
