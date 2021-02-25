frase = str(input('Digite uma frase ')).lower().strip()
a = frase.count('a')
ppos = frase.find('a') + 1
upos = frase.rfind('a') + 1
print('Na sua frase a palavra A aparece {} vezes'.format(a))
print('Em sua frase a primeira letra A aparece na posição {}'.format(ppos))
print('Em sua frase a ultima letra A aparece na posição {}'.format(upos))
