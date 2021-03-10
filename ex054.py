from datetime import date
total_maior = 0
total_menor = 0


for pessoas in range(1, 8):
    ano = int(input('Qual o ano de Nascimento da {}° Pessoa? '.format(pessoas)))
    idade = date.today().year - ano
    if idade >= 18:
        total_maior = total_maior + 1
    else:
        total_menor = total_menor + 1
print('Nesta opções temos {} pessoas maiores e {} pessoas menores.'.format(total_maior, total_menor))
