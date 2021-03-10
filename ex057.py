sexo = str(input('Informe o seu Sexo: [M/F]')).upper()
while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Tente Novamente! [M/F] ')).upper()
if sexo == 'M':
    print('Você é do sexo Masculino, Correto?')
elif sexo == 'F':
    print('Você é so dexo Feminino, Correto?')
