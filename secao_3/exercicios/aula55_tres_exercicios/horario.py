horario = input('Digite que horas são (HH:MM): ')

try:
    horas = int(horario.split(':')[0])
    if 0 <= horas < 12:
        print('Bom dia!')
    elif 12 <= horas < 18:
        print('Boa tarde!')
    elif 18 <= horas < 24:
        print('Boa noite!')
    else:
        print('Hora inválida, por favor digite um horário entre 00:00 e 23:59.')
except:
    print('Erro: Por favor, digite um horário válido no formato HH:MM.')