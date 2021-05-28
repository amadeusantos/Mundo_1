lar = float(input('Qual a largura da parede em m: '))
alt = float(input('Qual a altura da parede em m: '))
área = lar * alt
print(f'Sua parede possui dimensão {lar}X{alt} e uma área de {área}m².')
print(f'Serão necessários {área / 2}L de tinta para pintar essa parede.')
