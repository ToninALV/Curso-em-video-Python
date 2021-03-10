print('\033[36m-=-' * 10)
print('\033[1;97m    CALCULADORA PROGRAMAVEL')
print('\033[36m-=-' * 10)
print('')
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

print("""\033[1;97m
[1] Somar
[2] Subtrair
[3] Multiplicação
[4] Divisão
[5] Trocar os números
[6] Sair do Programa
""")

opção = int(input('\033[36mQual vai ser sua opção ?'))


if opção == 1:
    print('A soma de {} + {} = {}'.format(n1, n2, (n1 + n2)))


if opção == 2:
    print('O Resultado de {} - {} = {}'.format(n1, n2, (n1 - n2)))


if opção == 3:
    print('O Produto de {} * {} = {}'.format(n1, n2, (n1 * n2)))


if opção == 4:
    print('O Quociente de {} / {} = {}'.format(n1, n2, (n1/n2)))

while opção != 5:
    if opção == 5:


if opção == 6:
    print('Você decifiu fechar o programa. ADEUS!')








