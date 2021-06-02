nome = str(input('Qual seu nome completo: ')).strip().split()
print(f'Prazer em te conhecer.')
print(f'Seu primeiro nome é {nome[0]};')
print(f'Seu último nome é {nome[-1]}.')     # {nome[len(nome) - 1]}
