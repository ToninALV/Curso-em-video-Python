mais18 = qtdhomem = mulheresmenos20 = 0
while True:
    sexo = str(input('Qual o seu sexo? [M/F]: ')).upper()
    idade = int(input('Digite sua idade: '))
    print('Dados Cadastrados com sucesso.')
    option = str(input('Deseja cadastrar uma nova pessoa? [S/N]')).upper()
    if sexo == "F":
        if idade >= 18:
            mais18 += 1
        if idade < 20:
            mulheresmenos20 += 1
    if sexo == 'M':
        qtdhomem += 1
        if idade > 18:
            mais18 += 1
    if option == 'S':
        print('Ok. Digite os novos dados...')
    elif option == 'N':
        print('Ok')
        print('{} pessoas tem mais de 18 anos.'.format(mais18))
        print('Foram cadastrados {} homens.'.format(qtdhomem))
        print('Tem {} mulheres com menos de 20 anos.'.format(mulheresmenos20))
        break