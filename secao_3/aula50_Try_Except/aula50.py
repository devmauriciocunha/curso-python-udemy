"""
Introdução ao Try/Except

try: é utilizado para envolver um bloco de código que pode gerar uma exceção.
except: é utilizado para capturar e tratar a exceção gerada no bloco try.



print(1234)
print(456)
int('a')  # Isso vai gerar um erro, pois 'a' não pode ser convertido para inteiro
print(789)  # Este código não será executado devido ao erro anterior
"""

numero_str = input("Digite um número: ")

try:
    numero_float = float(numero_str)
    print('FLOAT:', numero_float)
    print(f'O dobro de {numero_float} é {numero_float * 2}')

except:
    print('Erro: Por favor, digite um número válido.')