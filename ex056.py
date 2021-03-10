soma_idade = 0
media_idade = 0
nome_velho = ''
maior_idade_homem = 0
total_mulheres20 = 0

for p in range(1, 5):
    print('\033[1;35m-----{}ª Pessoa-----'.format(p))
    nome = str(input('\033[1;97mNome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]')).lower()
    soma_idade = soma_idade + idade
    if p == 1 and sexo in 'm':
        maior_idade_homem = idade
        nome_velho = nome
    if sexo in 'm' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_velho = nome
    if sexo in 'f' and idade < 20:
        total_mulheres20 = total_mulheres20 + 1
print('')

media_idade = soma_idade / 4
print('A média de idade é {:.0f} anos.'.format(media_idade))
print('O Nome do homem mais velho é {} e ele tem {} anos.'.format(nome_velho, maior_idade_homem))
print('A quantidade de mulheres com idade abaixo de 20 é {}.'.format(total_mulheres20))
