
maisdemil = 0
totalgasto = 0
maisbarato = 0
cont = 0
barato = ''
while True:
    produto = str(input('Digite aqui o nome do Produto: '))
    valor = float(input('Digite aqui o valor deste produto: R$'))
    opção = str(input('Deseja adicionar mais produtos? [S/N]: ')).upper()
    cont += 1
    totalgasto += valor
    if valor > 1000:
        maisdemil += 1
    if cont == 1:
        maisbarato = valor
        barato = produto
    else:
        if valor < maisbarato:
            maisbarato = valor
            barato = produto
            resp = ' '
        print('')
    if opção == 'S':
        pass

    elif opção == 'N':
        totalgasto += valor
        print('')
        print('O Valor Total da compra é R${:.2f}'.format(totalgasto))
        print('Custaram mais de R$1.000, {} produtos.'.format(maisdemil))
        print('O produto mais barato foi {} e seu valor é de R${:.2f}'.format(barato, maisbarato))
        break
