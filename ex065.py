

opção = 'S'
qtdvalores = somavalores = maiorvalor = menorvalor = 0



while opção in 'S':
    n = int(input('Digite um número: '))
    qtdvalores += 1
    somavalores += n
    if qtdvalores == 1:
        maiorvalor = menorvalor = n

    else:
        if n > maiorvalor:
            maiorvalor = n
        if n < menorvalor:
            menorvalor = n
    opção = str(input('Quer Continuar ? [S/N]: ')).upper()

media = somavalores / qtdvalores

print('Você digitou um total de {} valores, e a média entre eles é {:.2f}'.format(qtdvalores, media))
print('O Maior número digitado foi {} e o Menor foi {}'.format(maiorvalor, menorvalor))



