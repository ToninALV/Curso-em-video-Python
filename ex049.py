print('\033[1;97m-=-' *5, '\033[1;36mTABUADA V2', '\033[1;97m-=-' *5)
print('')
valor = int(input('Digite um número e será mostrado sua Tabuada '))
print('')
for tabuada in range(1, 11):
    print('{} x {} = {}'.format(valor, tabuada,valor*tabuada))
