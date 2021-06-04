from datetime import date

ano = int(input('Digite o ano desejado para saber se ele é bissexto(Digite 0 para saber o ano atual): '))
if ano == 0:
    ano = date.today().year
if ano % 400 == 0 or ano % 4 == 0 and ano % 100 != 0:
    print(f'O ano {ano} é bissexto.')
else:
    print(f'O ano {ano} não é bissexto.')
