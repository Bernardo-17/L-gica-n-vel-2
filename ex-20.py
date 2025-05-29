hora_de_inicio = int(input('Digite o horario de inicio: '))
hora_de_termino = int(input('Digite o horario de termino: '))
if hora_de_inicio > hora_de_termino:
    print(24-(hora_de_inicio - hora_de_termino))
else:
    print(hora_de_termino - hora_de_inicio)
