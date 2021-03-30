termo = int(input('Digite o primeiro Termo: '))
razao = int(input('Agora digite a Razão: '))
decimo = termo + (10 - 1) * razao

while decimo > 0:
    print('{}'.format(decimo), end='->' )
    break
print('ACABOU')