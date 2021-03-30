totalnumero = 0
somanumero = 0

n = 0
while n < 999:
    if n >= 0 and n < 999:
        somanumero += n
        n = int(input('Digite um número. [999 para parar]: '))
        totalnumero += 1


    else:
        print('Opção Inválida. Tente Novamente!!!')



print('Você digitou um total de {} números, e a soma deles é {}'.format(totalnumero - 1, somanumero ))