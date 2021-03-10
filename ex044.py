print('{:=^40}'.format(' LOJAS TONINHO '))
print('')
valor = float(input('Qual o valor do produto R$'))
print('')

print('[1] à vista DINHEIRO/CHEQUE')     #10%desconto
print('[2] à vista CARTÃO')              #5%desconto
print('[3] até 2x no CARTÃO')            #preço formal
print('[4] 3x ou mais no CARTÃO')        #20%juros
print(' ')
res = int(input('De que modo será realizado o pagamento?'))
print(' ')
if res == 1:
    valor_final = valor * 0.10
    valor_final2 = valor - valor_final
    print('A opção escolhida gera um desconto de 10%')
    print('O valor final de seu produto é R${}'.format(valor_final2))
    print('Você economizou um total de R${}'.format(valor_final))
elif res == 2:
    valor_final = valor * 0.05
    valor_final2 = valor - valor_final
    print('A opção escolhida gera um desconto de 5%')
    print('O valor final de seu produto é R${}'.format(valor_final2))
    print('Você economizou um total de R${}'.format(valor_final))
elif res == 3:
    print('A opção escolhida não gera nenhum desconto.')
    print('O valor final de seu produto é R${}'.format(valor))
elif res == 4:
    parcela = int(input('Quantas vezes você quer parcelar esse pagamento? '))
    valor1 = valor * 1.2
    parcela_mes = valor1 / parcela
    print('A opção escolhida contém juros!')
    print('O valor final de seu produto é R${}'.format(valor1, parcela))
    print('O valor de cada parcela será de R${} por mês'.format(parcela_mes))
else:
    print('Opção INVÁLIDA DE PAGAMENTO. Tente Novamente!')
