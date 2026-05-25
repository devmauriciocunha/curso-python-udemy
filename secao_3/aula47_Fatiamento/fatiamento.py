"""
fatiamento de strings

012345678
Olá, Mundo!
-987654321
fatiamento [ini:fim:passo] [i:f:p]
Obs.: a função len retorna a quantidade de caracteres da string, incluindo espaços
"""

variavel = 'Olá, Mundo!'
print(variavel[0:5])  # Olá, (do índice 0 até o índice 4, o índice 5 não é incluído)
print(variavel[6:])   # Mundo! (do índice 6 até o final da string)
print(variavel[:5])   # Olá, (do início da string até o índice 4)
print(variavel[::2])  # O,Mn! (do início ao fim da string, pulando de 2 em 2 caracteres)
print(variavel[::-1]) # !odnuM ,álO (do fim ao início da string, invertendo a ordem dos caracteres)
print(len(variavel))  # 13 (quantidade de caracteres na string, incluindo espaços)