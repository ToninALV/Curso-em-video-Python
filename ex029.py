
print('-_-' *10)
print('-----RADAR DE VELOCIDADE-----')
print('-_-' * 10)
velocidadeatual = float(input('Qual a sua velocidade Atual ? '))
multa = velocidadeatual - 80
valormulta = multa * 7

if velocidadeatual <= 80:
    print('---BOM DIA---!')
    print('TENHA UMA ÓTIMA VIAGEM')
    print('OBRIGADO POR RESPEITAR A VELOCIDADE PERMITIDA')
else:
    print('VOCÊ FOI MULTADO EM UM VALOR DE R${}'.format(valormulta))
    print('DIMINUA SUA VELOCIDADE !')
    print('A VELOCIDADE PERMITIDA PARA ESSA PISTA É 80Km/h !')
