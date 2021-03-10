from time import sleep
tot = 0
n1 = int(input('Digite um número: '))
print('\033[1;97mIremos mostrar se esse número é primo ou não.')
sleep(1)
for c in range(1, n1 +1):
    if n1 % c == 0:
        print('\033[34m', end='')
        tot = tot + 1
    else:
        print('\033[m', end='')
    print('{} '.format(c), end='')
print('\n\033[mO número {} foi divido {} vezes'.format(n1, tot))
if tot == 2:
    print('')
    print('E por isso ele é PRIMO')
else:
    print('')
    print('E por isso ele NÃO é PRIMO')