salario_base = float(input('Qual é o salario atual do Funcionário? R$'))

if salario_base <= 1250:
    salario15 = salario_base * 1.15
    print('O ajuste salaria fara com que você receba R${:.2f}'.format(salario15))
else:
    salario10 = salario_base * 1.10
    print('O ajuste salarial fara com que você receba R${:.2f}'.format(salario10))
