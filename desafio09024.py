cidade = str(input('Qual o nome de sua cidade: ')).strip().lower()
print(f'Sua cidade começa com nome Santo: '
      f'{cidade.split()[0] == "santo"}.'.replace('True', 'Sim').replace('False', 'Não'))    # {cidade[:5] == "santo"}
# 3 {cidade.find("santo") == 0}
