from datetime import date
ano = int(input('Qual ano você deseja que eu verifique se é BISSEXTO ou Não ?  Digite 0 para verificar o ano em que você esta ! '))
if ano == 0:
    ano = date.today().year

if ano % 100 != 0 and ano % 4 == 0 or ano % 400 == 0:
    print('O Ano {} é BISSEXTO'.format(ano))

else:
    print('O Ano {} não é BISSEXTO'.format(ano))

