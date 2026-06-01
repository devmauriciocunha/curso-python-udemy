import unicodedata

frase = 'O Python é uma linguagem de programação '\
        'multiparadigma. '\
        'Python foi criado por Guido van Rossum.'

i = 0

while i < len(frase):
    frase = unicodedata.normalize('NFD', frase) #normaliza a string, ou seja, remove os acentos e outros caracteres especiais.
    frase = frase.lower().replace(' ', '') #converte a string para minúscula, para que a contagem de letras seja case-insensitive.
    letra = frase[i]
    contagem = frase.count(letra)
    print(f'A letra "{letra}" aparece {contagem} vezes na frase.')
    i += 1