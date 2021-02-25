distancia = float(input('Qual a distância de sua viagem ? '))

if distancia <= 200:
    preco = distancia * 0.50
    print('-----VOCÊ IRA COMEÇAR UMA VIAGEM-----')
    print('Sua viagem ira custar um total de R${:.2f}'.format(preco))

else:
    preco2 = distancia * 0.45
    print('-----VOCÊ IRA COMEÇAR UMA VIAGEM COM UM VALOR PROMOCIONAL-----')
    print('Sua viagem ira custar um total de R${:.2f}'.format(preco2))



