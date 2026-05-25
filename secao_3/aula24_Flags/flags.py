"""
Flags são usados para indicar o estado de algo, ou seja, se algo está ativo ou inativo. 
Eles são comumente usados em programação para controlar o fluxo de execução de um programa, 
indicando se uma determinada condição é verdadeira ou falsa.

None = nâo valor, ou seja, o valor é desconhecido ou não aplicável
is e is not = é ou não é o mesmo objeto, ou seja, compara a identidade dos objetos
id = Identidade do objeto, ou seja, o endereço de memória do objeto

declarar variável fora do bloco if para evitar erros de variável não definida

"""

condicao = True  # Exemplo de condição, pode ser True ou False
passou_no_if = None  # Declarando a variável fora do bloco if

if condicao:
    passou_no_if = True  # Atribuindo um valor à variável dentro do bloco if
    print('Faça algo')
else:
    print('Não faça algo')

print(passou_no_if, passou_no_if is None)  # Agora podemos acessar a variável mesmo fora do bloco if, pois ela foi declarada anteriormente
print(passou_no_if, passou_no_if is not None)  # Verificando se a variável passou_no_if é diferente de None, ou seja, se ela foi atribuída a um valor dentro do bloco if