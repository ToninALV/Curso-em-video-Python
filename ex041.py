from datetime import date

nasc = int(input('Digite seu ano de nascimento, e iremos mostrar sua categoria.'))
ano_atual = date.today().year
idade = ano_atual - nasc

if idade < 0 and idade <= 9:
    print('MIRIM')
    print('Você tem {} anos'.format(idade))

elif idade > 9 and idade <= 14:
    print('INFANTIL')
    print('Você tem {} anos'.format(idade))

elif idade > 14 and idade <= 19:
    print('JÚNIOR')
    print('Você tem {} anos'.format(idade))

elif idade > 19 and idade <= 25:
    print('SÊNIOR')
    print('Você tem {} anos'.format(idade))

elif idade > 25:
    print('MASTER')
    print('Você tem {} anos'.format(idade))

