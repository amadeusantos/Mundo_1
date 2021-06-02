nome = str(input('Qual seu nome completo: ')).strip().lower()
print(f'Você possui Silva no nome: '
      f'{nome.count("silva") > 0}.'.replace('True', 'Sim').replace('False', 'Não'))     # {nome.find("silva") != -1}
# 3 {"silva" in nome}
