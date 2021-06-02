from random import sample

a1 = str(input('Qual o nome do primeiro aluno: '))
a2 = str(input('Qual o nome do segundo aluno: '))
a3 = str(input('Qual o nome do terceiro aluno: '))
a4 = str(input('Qual o nome do quarto aluno: '))
alunos = sample((a1, a2, a3, a4), 4)    # alunos = [a1, a2, a3, a4] # shuffle(alunos)
print(f'A ordem dos alunos sorteados foram {alunos}.')
