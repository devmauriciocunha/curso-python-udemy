"""
--- Operadores lógicos: and, or, not
* O operador lógico "and" é utilizado para combinar duas expressões booleanas. 
Ele retorna True somente se ambas as expressões forem verdadeiras. Caso contrário, ele retorna False.

Exemplo:
```python
a = True
b = False
resultado = a and b
print(resultado)  # Output: False
```

No exemplo acima, a expressão "a and b" retorna False porque a é True e b é False.
Outro exemplo:
```python
x = 5
y = 10
resultado = (x > 0) and (y > 0)
print(resultado)  # Output: True
```
Neste exemplo, a expressão "(x > 0) and (y > 0)" retorna True porque 
ambas as condições são verdadeiras (x é maior que 0 e y é maior que 0).



"""

if 1 and 1:
    print(True and 1 and False)