n1 = int(input('Digite um número para ser convertido: '))
print(' ')
print('Escolha qual vai ser a base da conversão')
print(' ')
print('[ 1 ] converter para BINARIO')
print('[ 2 ] converter para OCTAL')
print('[ 3 ] converter para HEXADECIMAL')
print(' ')
op1 = int(input('Qual é a base da conversão ?'))

if op1 == 1:
    bin = bin(n1)
    print('Este número em BINARIO é {}'.format(bin[2:]))

elif op1 == 2:
    oct = oct(n1)
    print('Este número em OCTAL é {}'.format(oct[2:]))

elif op1 == 3:
    hex = hex(n1)
    print('Este número em HEXADECIMAL é {}'.format(hex[2:]))
else:
    print('Opção Invalida. Tente novamente.')


