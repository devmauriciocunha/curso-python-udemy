nome = input('Digite seu nome: ').strip()


if any(char.isdigit() for char in nome):
    print('Nome não pode conter número(s).')
elif nome == '':
    print('Nome não pode ser vazio.')
else:
    quantidade_de_letras = len(nome)
    if 0 < quantidade_de_letras <= 4:
        print('Seu nome é curto')
    elif 5 <= quantidade_de_letras <= 6:
        print('Seu nome é normal')
    else:
        print('Seu nome é muito grande')
    
