frase = str(input('Digite uma frase: ')).strip().lower()
print(f'Na frase digitada a {frase.count("a")} letras "a"s;')
print(f'A primeira letra "a" aparece na posição {frase.find("a") + 1} e a última na posição {frase.rfind("a") + 1}.')
