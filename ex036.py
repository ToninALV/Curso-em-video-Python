print('\033[1;32m-=-\033[1;32m' * 11)
print('\033[1;97m   APROVADOR DE FINANCIAMENTOS\033[1;97m')
print('\033[1;32m-=-\033[1;32m' * 11)

valor_casa = float(input('\033[1;96mQual o valor da casa? R$'))
valor_salario = float(input('\033[1;96mQuanto você recebe de salário? R$'))
quantidade_anos = int(input('\033[1;96mQuantos anos você ira demorar para pagar a casa? '))

valor_parcela = valor_casa / quantidade_anos / 12
quantidade_parcelas = quantidade_anos/12
valor_desconto = valor_salario * 30/100

if valor_parcela > (valor_salario-valor_desconto):
    print('')
    print('\033[1;31mNEGADO')
    print('\033[0;97mPedimos desculpas, mas o valor mensal excede 30% do seu salário!')
    print('\033[0;97mO valor de cada parcela seria de R${:.2f} por mês durante {:.0f} anos'.format(valor_parcela, quantidade_anos))
else:
    print('')
    print('\033[1;32mAPROVADO')
    print('\033[0;97mVocê ira pagar uma valor de R${:.2f} por mês durante {:.0f} anos!'.format(valor_parcela, quantidade_anos))


