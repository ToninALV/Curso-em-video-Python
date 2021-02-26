print('Digite as notas de sua prova Bimestral e sua Avaliação Somativa.')

somativa = float(input('Avaliação Somativa: '))
bimestral = float(input('Prova Bimestral: '))

media = (somativa + bimestral)/2

if media >= 7:
    print('\033[1;32mAPROVADO\033[1;32m')
    print('Sua média foi de {:.1f}'.format(media))


elif media < 5:
    print('\033[1;31mREPROVADO\033[1;31m')
    print('Sua média foi de {:.1f}'.format(media))


elif media >= 5 and media < 7:
    print('\033[1;36mRECUPERAÇÃO\033[1;36m')
    print('Sua média foi de {:.1f}'.format(media))
