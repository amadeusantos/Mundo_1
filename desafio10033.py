n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
maior = n1
menor = n1
if maior < n2:
    maior = n2
if maior < n3:
    maior = n3
if menor > n2:
    menor = n2
if menor > n3:
    menor = n3
# nums = [n1, n2, n3]
# maior = max(nums)
# menor = min(nums)
print(f'O maior número digitado foi {maior} e o menor foi {menor}.')
