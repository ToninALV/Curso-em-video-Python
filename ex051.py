termo = int(input('Digite o primeiro termo: '))
razao = int(input('Agora digite a Razão: '))
decimo = termo + (10 - 1) * razao

for c in range(termo,decimo + razao, razao):
    print('{} '.format(c), end='-> ')
print('ACABOU')

