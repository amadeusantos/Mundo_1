algo = input('Digite algo: ')
print(f'É formado somente por letras e números: {algo.isalnum()}')
print(f'É formado somente por digitos: {algo.isdigit()}')
print(f'É formado somente por espaços: {algo.isspace()}')

print(f'É formado só por letras: {algo.isalpha()}')
print(f'Esta capitalizado: {algo.istitle()}')
print(f'É formado só por letras maiúsculas: {algo.isupper()}')
print(f'É formado só por letras minúsculas: {algo.islower()}')

print(f'É formado só por números: {algo.isnumeric()}')
print(f'É um número decimal: {algo.isdecimal()}')

print(f'Todos o caracteres são do padrão ASCII: {algo.isascii()}')
print(f'Pode ser impresso na tela: {algo.isprintable()}')
print(f'Pode se um identificador válido: {algo.isidentifier()}')
