print('\033[1;31m-=-' *10)
print(""" 
        \033[1;97mANALISADOR 
            \033[1;35mDE 
        \033[1;36mTRIANGULOS 
            \033[1;33mV2""")
print(' ')
print('\033[1;031m-=-' *10)
print('\033[0;0m')
v1 = float(input('Digite um valor: '))
v2 = float(input('Digite outro valor: '))
v3 = float(input('Digite outro valor: '))
print(''' 
''')

if v1 < v2 + v3 and v2 < v1 + v3 and v3 < v1 + v2:
    print('\033[1;97mEsses valores podem formar um triângulo, Esse triangulo é; ')

    if v1 != v2 and v2 != v3 and v1 != v3:
        print('\033[1;31mESCALENO')


    elif v1 == v2 and v2 == v3 and v3 == v1:
        print('\033[1;36mEQUILÁTERO')


    else:
        print('\033[1;33mISÓCELES')

else:
    print('\033[1;97mEsses valores não podem formar um triângulo.')






