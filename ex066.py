qtdvalores = soma = 0

while True:
    n = int(input('Digite um número. [999 para parar]: '))
    if n == 999:
        break
    qtdvalores += 1
    soma += n
print(f'Você digitou um total de {qtdvalores} valores, e a soma deles é {soma}.')
