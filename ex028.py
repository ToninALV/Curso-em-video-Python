import random
import colorsys
import time
print('-=-' *20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' *20)
randomn = random.randrange(0, 5)
#sorte = input(int('Qual sera o número de sua tentativa ?')
#sorte=input(int('Qual será sua tentativa ?'))
sorte=int(input('Qual será sua tentativa ? '))
print('PROCESSANDO...')
time.sleep(2)

if randomn == sorte:
    print('PARABÉNS VOCÊ GANHOU !!!')

else:
    print('QUE PENA VOCÊ ERROU, TENTE NOVAMENTE !!!')
    print('O número pensado por mim, foi {}' .format(randomn))

