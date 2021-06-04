from random import randint

pc = randint(0, 5)
pessoa = int(input('Eu acabei de pensar em um número entre 0 e 5, tente adivinhar qual foi: '))
# print(f'Parabéns, você acertou!!!' if pc == pessoa else f'Que pena, você errou! eu pensei no número {pc}.')
if pc == pessoa:
    print(f'Parabéns, você acertou!!!')
else:
    print(f'Que pena, você errou! eu pensei no número {pc}.')
print(f'Obrigado por brincar!')
