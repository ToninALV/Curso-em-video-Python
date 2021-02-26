from datetime import date

ano = int(input('Quer saber quando deve se alistar? Digite o ano em que você nasceu '))

ano_atual = date.today().year
restante = ano - ano_atual
idade = ano_atual - ano
quanto_falta = 18 - idade
print(' ')
print('Quem nasceu em {} tem {} anos em {}'.format(ano, idade, ano_atual))
print(' ')

if ano_atual - ano < 18:
    print('Você ainda é novo, aproveite seu tempo, faltam {} anos para você se alistar'.format(quanto_falta))
elif ano_atual - ano > 18:

    quanto_falta = idade - 18
    print('''URGENTE
Você já tinha que ter se alistado á {} anos, Vá se alistar AGORA!'''.format(quanto_falta))

else:
    print('Vá logo fazer seu alistamento, está na hora exata!')





