"""
Continue é uma palavra reservada em Python que é usada dentro de loops (como while ou for) 
para pular a iteração atual e continuar com a próxima iteração do loop. 
Quando o interpretador encontra a palavra-chave continue, ele ignora o 
restante do código dentro do loop para aquela iteração específica e volta 
para o início do loop para verificar a condição novamente.

"""

contador = 0

while contador < 100:
    contador += 1
    
    if contador % 2 == 0:
        continue
    print(contador)

print('Acabou')