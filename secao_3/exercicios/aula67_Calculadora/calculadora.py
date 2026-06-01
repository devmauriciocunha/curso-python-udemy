print('Calculadora Simples')

while True:
    
    num1 = input('Digite o primeiro número: ')
    operador = input('Digite o operador (+, -, *, /): ')
    num2 = input('Digite o segundo número: ')

    numeros_validos = None


    try:
        num1 = float(num1)
        num2 = float(num2)
        numeros_validos = True
    except ValueError:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos. Tente novamente.')
        continue

    operadores_permitidos = ['+', '-', '*', '/']
    if operador not in operadores_permitidos:
        print('Operador inválido. Tente novamente.')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador. Tente novamente.')
        continue
    

    if operador == '+':
        resultado = num1 + num2
    elif operador == '-':
        resultado = num1 - num2
    elif operador == '*':
        resultado = num1 * num2
    elif operador == '/':
        if num2 == 0:
            print('Não é possível dividir por zero. Tente novamente.')
            continue
        resultado = num1 / num2
    
    print(f'O resultado de {num1} {operador} {num2} é: {resultado}')


    sair = input('Deseja sair? (s/n) ').lower()
    sair = sair.startswith('s') #startswith retorna um booleano, ou seja, True ou False. 
    # No caso, se o usuário digitar 's' ou 'sim', a variável 'sair' será True, caso contrário, será False.
    if sair is True:
        print('Saindo...')
        print('Até mais!')
        break