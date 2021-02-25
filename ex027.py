nome = str(input('Digite seu nome completo ')).strip()
n= nome.split()
print('Seu primeiro nome é {}' .format(nome.split(' ')[0]))
print('E seu ultimo nome é {}' .format(n[len(n)-1]))
