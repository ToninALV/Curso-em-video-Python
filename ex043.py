print('\033[1;36m-=-\033[1;36m'*5)
print('\033[1;31m  Calculadora\033[1;31m')
print('\033[1;31m      IMC\033[1;31m')
print('\033[1;36m-=-\033[1;36m'*5)


peso = float(input('\033[0;97mQual o seu Peso em KG? '))
altura = float(input('Qual a sua altura em M?\033[0;97m'))
print('')
imc = peso / (altura**2)

if imc < 18.5:
    print('\033[1;31mSeu IMC é {:.2f}, você está abaixo do Peso!'.format(imc))
elif imc > 18.5 and imc < 25:
    print('\033[1;32mSeu IMC é {:.2f}, você está no peso Ideal!'.format(imc))
elif imc >= 25 and imc <= 40:
    print('\033[1;33mSeu IMC é {:.2f}, você está Obeso!'.format(imc))
else:
    print('\033[1;34mSeu IMC é {:.2f}, você está com Obesidade Mórbida!!!'.format(imc))



