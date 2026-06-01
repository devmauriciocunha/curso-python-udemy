nome = 'Maria Silva'

tamanho_nome = len(nome)
print(nome, tamanho_nome)
contagem = 0
novo_nome = ''
while contagem < tamanho_nome:
    letra = nome[contagem]
    novo_nome += f'*{letra}'
    contagem += 1

print(novo_nome)