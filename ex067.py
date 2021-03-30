print('-' * 15)
print(' Tabuava v3.0')
print('-' * 15)

while True:
    print('')
    n = int(input('Digite o número que você deseja ver a tabuada: '))
    print('')
    print('-' * 15)
    if n > 0:
        for c in range(1, 11):
            soma = n * c
            print('{} * {} = {}'.format(n, c, soma))
        print('-' * 15)
    else:
        break
print('PROGRAMA TABUADA ENCERRADO. VOLTE SEMPRE!')

