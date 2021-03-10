maior = 0
menor = 0

for p in range(1, 6):
    peso = float(input('Qual o peso da {}° Pessoa? '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print('O maior peso é {}Kg, e o menor peso é {}Kg.'.format(maior, menor))
