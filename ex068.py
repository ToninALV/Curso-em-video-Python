from random import randint
from time import sleep

qtdwins = 0

while True:
    número = int(input('Digite um Número: '))
    opção = str(input('[P/I]: ')).upper()
    computador = randint(0, 10)
    soma = número + computador
    if opção == 'P':
        if (soma % 2) == 0:
            print('Você Jogou {} e o computador {}. Total {}, DEU PAR.'.format(número, computador, soma))
            print('Você Venceu!')
            print('Vamos jogar Novamente...')
            sleep(0.5)
            qtdwins += 1
        else:
            print('Você Jogou {} e o computador {}. Total {}, DEU ÍMPAR.'.format(número, computador, soma))
            print('Computador Venceu!')
            print('')
            print('GAME OVER, Você teve {} Vitórias Seguidas.'.format(qtdwins))
            break
    if opção == 'I':
        if (soma % 2) == 0:
            print('Você jogou {} e o computador {}. Total {}, DEU PAR.'.format(número, computador, soma))
            print('Computador Venceu!')
            print('')
            print('GAME OVER, Você teve {} Vitórias Seguidas.'.format(qtdwins))
            break
        else:
            print('Você Jogou {} e o computador {}. Total {}, DEU ÍMPAR.'.format(número, computador, soma))
            print('Você Venceu!')
            print('Vamos jogar Novamente...')
            sleep(0.5)
            qtdwins += 1



