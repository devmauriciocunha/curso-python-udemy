"""
Operadores in e not in

    Os operadores "in" e "not in" são utilizados para verificar a presença ou 
ausência de um elemento em uma sequência, como uma lista, tupla, string ou conjunto.

Strings são interáveis, ou seja, podem ser percorridas caractere por caractere.
Exemplo com string:
```python
frase = "Olá, mundo!"
if "mundo" in frase:
    print("A palavra 'mundo' está presente na frase.")
else:
    print("A palavra 'mundo' não está presente na frase.")
```
No exemplo acima, a expressão "'mundo' in frase" retorna True porque a 
palavra "mundo" está presente na string "Olá, mundo!".

Exemplo com lista:
```python
numeros = [1, 2, 3, 4, 5]
if 3 in numeros:
    print("O número 3 está presente na lista.")
else:
    print("O número 3 não está presente na lista.")
```
No exemplo acima, a expressão "3 in numeros" retorna True porque o número 3
está presente na lista [1, 2, 3, 4, 5].

----------------------------------------------------------------------------------------


O operador "not in" é utilizado para verificar a ausência de um elemento em uma sequência.
Exemplo com string:
```python
frase = "Olá, mundo!"
if "Python" not in frase:
    print("A palavra 'Python' não está presente na frase.")
else:
    print("A palavra 'Python' está presente na frase.")
```
No exemplo acima, a expressão "'Python' not in frase" retorna True porque a
palavra "Python" não está presente na string "Olá, mundo!".

Exemplo com lista:
```python
numeros = [1, 2, 3, 4, 5]
if 6 not in numeros:
    print("O número 6 não está presente na lista.")
else:
    print("O número 6 está presente na lista.")
```
No exemplo acima, a expressão "6 not in numeros" retorna True porque o número 6
não está presente na lista [1, 2, 3, 4, 5].

"""

nome = 'Alice'
print('A' in nome)  # Output: True
print(10*'---')
print('B' in nome)  # Output: False
print(10*'---')
print('C' not in nome)  # Output: True
print(10*'---')
print('ice' in nome)  # Output: True
print(10*'---')
