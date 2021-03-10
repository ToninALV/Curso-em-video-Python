soma = 0
for n in range(1, 7):
    n1 = int(input('Digite o {}° número: '.format(n)))
    if n1 % 2 == 0:
        soma = soma + n1
print('A soma dos número pares é {}'.format(soma))


