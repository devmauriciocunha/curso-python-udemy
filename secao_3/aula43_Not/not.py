"""
Operador NOT
    O operador NOT é um operador lógico que inverte o valor de um operando. 
Ele é representado pelo símbolo "not" em Python.

Exemplo:
```python
a = True
resultado = not a
print(resultado)  # Output: False
```
No exemplo acima, a expressão "not a" retorna False porque a é True.

Not inverte o valor de uma expressão booleana. 
Se a expressão for True, o resultado será False, e vice-versa.

"""

senha = input("Digite a senha: ")

if not senha:
    print("A senha não pode ser vazia.")