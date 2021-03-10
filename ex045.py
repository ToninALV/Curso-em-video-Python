import random
import time

print('\033[1;31m{:=^40}'.format(' JOKENPO \033[1;31m'))
print("""\033[1;36m
[0] PEDRA
[1] PAPEL
[2] TESOURA
      """)
computador = random.randint(0, 2)
print('')
jogador = int(input('\033[1;97mEscolha uma das opções: '))
print('')
time.sleep(0.2)
print('\033[1;95mJO')
time.sleep(0.5)
print('\033[1;94mKEN')
time.sleep(0.5)
print('\033[1;93mPO')
print('')
itens = ('PEDRA', 'PAPEL', 'TESOURA')
print('\033[1;97m-=-'*11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=-'*11)
print('')
if computador == 0: # Computador jogou PEDRA
    if jogador == 0: # Jogador jogou PEDRA
        print('\033[1;33m   EMPATE')
        print('\033[0;97m{} = {}'.format(itens[computador], itens[jogador]))


    elif jogador == 1: # Jogador jogou PAPEL
        print('\033[1;97mJogador \033[1;92m\033[1;31mVENCEU')
        print('\033[0;97m{} < {}'.format(itens[computador], itens[jogador]))


    elif jogador == 2: # jogador jogou TESOURA
        print('\033[0;97mComputador \033[1;31mVENCEU')
        print('\033[0;97m{} > {}'.format(itens[computador], itens[jogador]))


elif computador == 1: #Computador jogou PAPEL
    if jogador == 0:# Jogador jogou PEDRA
        print('\033[0;97mComputador \033[1;31mVENCEU')
        print('{} > {}'.format(itens[computador], itens[jogador]))


    elif jogador == 1:# Jogador jogou PAPEL
        print('\033[0;33mEMPATE')
        print('\033[0;97m{} = {}'.format(itens[computador], itens[jogador]))


    elif jogador == 2:# jogador jogou TESOURA
        print('\033[0;97mJogador \033[1;31mVENCEU')
        print('\033[0;97m{} < {}'.format(itens[computador], itens[jogador]))


elif computador == 2: #Computador jogou TESOURA
    if jogador == 0:# Jogador jogou PEDRA
        print('\033[0;97mJogador \033[1;31mVENCEU')
        print('\033[0;97m{} < {}'.format(itens[computador], itens[jogador]))


    elif jogador == 1:# Jogador jogou PAPEL
        print('\033[0;31mComputador \033[1;31mVENCEU')
        print('\033[0;97m{} > {}'.format(itens[computador], itens[jogador]))


    elif jogador == 2:# jogador jogou TESOURA
        print('\033[1;33mEMPATE')
        print('\033[0;97m{} = {}'.format(itens[computador], itens[jogador]))