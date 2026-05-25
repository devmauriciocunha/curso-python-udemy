nome = input("Digite seu nome: ")



if not nome:  # Verifica se o nome é vazio ou contém apenas espaços
    print("Você não digitou um nome.")

elif nome.isdigit():  # Verifica se o nome contém apenas números
    print("O nome não pode digitar números.")
else:
    invertido = nome[::-1]
    quantidade_letras = len(nome.replace(" ", ""))  # Remove os espaços para contar apenas as letras
    primeira_letra = nome[0]
    ultima_letra = nome[-1]
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {invertido}')
    print(f'Seu nome tem {quantidade_letras} letras')
    print(f'A primeira letra do seu nome é {primeira_letra}')
    print(f'A última letra do seu nome é {ultima_letra}')
