"""
.<numero de digitos>f
x ou X - para hexadecimal
o - para octal
b - para binário
> - para alinhamento à direita
< - para alinhamento à esquerda
^ - para centralizar
Sinal - + ou - para exibir o sinal positivo ou negativo
Ex.: 0>-100,.2f
Conversion flags:
!r - para usar a representação de string do objeto (repr())
!s - para usar a representação de string do objeto (str())
!a - para usar a representação de string do objeto (ascii())

"""

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')  # Alinhamento à direita
print(f'{variavel: <10}')  # Alinhamento à esquerda
print(f'{variavel: ^10}')  # Centralizado
print(f'{variavel:*>10}')  # Alinhamento à direita com preenchimento de asteriscos
print(f'{variavel:!^20}')  # Centralizado com preenchimento de exclamações
print(f'{variavel!r}')  # Usando a representação de string do objeto (repr())
print(f'{variavel!s}')  # Usando a representação de string do objeto (str())
print(f'{variavel!a}')  # Usando a representação de string do objeto (  ascii())