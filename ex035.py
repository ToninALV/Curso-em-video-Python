print('-=-'*10)
print('  \033[1;30mANALISADOR\033[1;30m \033[1;31mDE\033[1;31m \033[1;32mTRIÂNGULOS V1\033[1;32m')
print('-=-'*10)
print(' ')
print('-'*20)
print(' ')

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro Segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('\033[1;36mOs segmentos acima PODEM FORMAR triângulo!\033[1;36m')
else:
    print('\033[0;31mOs segmentos acima NÃO PODEM FORMAR triângulo!\033[0;31m')




