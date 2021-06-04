sálario = float(input('Qual o valor do seu sálario: R$'))
# novo = (sálario * 1.10) if sálario > 1250 else sálario * 1.15
if sálario > 1250:
    novo = sálario * 1.10
else:
    novo = sálario * 1.15
print(f'O valor do seu novo sálario será R${novo:.2f}.')
