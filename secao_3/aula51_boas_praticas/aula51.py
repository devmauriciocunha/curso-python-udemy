"""
Constantes no python

    Em Python, uma constante é um valor que não deve ser alterado durante a execução do programa.
Embora Python não tenha uma sintaxe específica para definir constantes, é uma convenção 
usar letras maiúsculas para indicar que uma variável é uma constante.

Exemplo:
```python
PI = 3.14159
GRAVIDADE = 9.81
```
No exemplo acima, PI e GRAVIDADE são constantes que representam o valor de pi e a aceleração da gravidade, respectivamente.
Embora seja possível alterar o valor dessas variáveis, a convenção de usar letras maiúsculas
indica que elas devem ser tratadas como constantes e não devem ser modificadas.

Boas práticas

Muitas condições no mesmo if (ruim)
```python
if idade >= 18 and idade <= 65 and salario > 2000:
    print("Você é elegível para o benefício.")
```
Melhor usar variáveis intermediárias para melhorar a legibilidade do código:
```python
maior_idade = idade >= 18
menor_idade = idade <= 65
salario_adequado = salario > 2000
if maior_idade and menor_idade and salario_adequado:
    print("Você é elegível para o benefício.")
```
Muitos blocos if aninhados (ruim)
```pythonif 
idade >= 18:
    if idade <= 65:
        if salario > 2000:
            print("Você é elegível para o benefício.")
```
Melhor usar operadores lógicos para evitar aninhamento excessivo:
```python
if idade >= 18 and idade <= 65 and salario > 2000:
    print("Você é elegível para o benefício.")
```

"""