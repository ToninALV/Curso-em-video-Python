from random import randint
totpalpitemais = 0
totpalpitemenos = 0
print('-=-' *20)
print('   Irei pensar em um número entre 0 e 10. Tente Adivinhar')
print('-=-' *20)
print('')
palpite  = int(input('Qual número você acha que é ? '))
computador = randint(0, 10)
while not palpite == computador:
    if palpite > computador:
        palpite = int(input('Muito Alto, Tente novamente: '))
        totpalpitemais += 1
    if palpite < computador:
        palpite = int(input('Muito baixo, Tente novamente: '))
        totpalpitemenos += 1

print('Parabéns o número que o computador pensou é {}...'.format(computador))
print('Foi necessário um total de {} Tentativas, para que você pudesse acertar.'.format(totpalpitemais + totpalpitemenos + 1))


