texto = str(input('Digite uma frase: '))

texto_sem_espaços = texto.replace(' ', '')
text_todo_minusculo = texto_sem_espaços.lower()
texto_invertido = text_todo_minusculo[::-1]
if texto_invertido == text_todo_minusculo:
    print('A frase {} de trás pra frente é {}, por isso ela é um palindromo.'.format(texto, texto_invertido))
else:
    print('A frase {} de trás pra frente é {}, por isso ela NÃO é um palindromo.'.format(texto, texto_invertido))
