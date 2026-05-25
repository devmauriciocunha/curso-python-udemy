print('Par ou Ímpar')
valor = input('Digite um número: ')

try:
    conversao = float(valor)
    if conversao % 2 == 0:
        print(f'O número {conversao} é par.')
    else:
        print(f'O número {conversao} é ímpar.')
except:
    print('Erro: Por favor, digite um número válido.')