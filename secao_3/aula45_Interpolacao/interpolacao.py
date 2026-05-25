"""
interpolação 

    A interpolação de strings é uma técnica que permite inserir 
valores de variáveis dentro de uma string de forma mais legível e conveniente.

Existem várias maneiras de realizar a interpolação de strings em Python,
mas uma das formas mais comuns é utilizando f-strings (formatted string literals),
que foram introduzidas no Python 3.6. As f-strings permitem que você 
insira expressões dentro de chaves {} e elas serão avaliadas e convertidas em strings automaticamente.

s -string
d e i -inteiros
f -números de ponto flutuante
Exemplo de interpolação com f-strings:
```python
nome = "Alice"
idade = 30
altura = 1.75
mensagem = f"Meu nome é {nome}, tenho {idade} anos e minha altura é {altura} metros."
print(mensagem)
```

"""

nome = "Alice"
preco = 19.99
variavel = '%s tem um produto que custa R$%.2f' % (nome, preco)
print(variavel)