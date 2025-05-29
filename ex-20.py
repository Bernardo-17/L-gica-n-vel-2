#20) Ler a hora de início e a hora de fim de um jogo de Xadrez (considere apenas horas inteiras, sem os minutos) e calcule a duração do jogo em horas, sabendo-se que o tempo máximo de duração do jogo é de 24 horas e que o jogo pode iniciar em um dia e terminar no dia seguinte
hora_de_inicio = int(input('Digite o horario de inicio: '))
hora_de_termino = int(input('Digite o horario de termino: '))
if hora_de_inicio > hora_de_termino:
    print(24-(hora_de_inicio - hora_de_termino))
else:
    print(hora_de_termino - hora_de_inicio)
#Na quinta linha tem como o resultado das diferença das variaveis menos 24 porque, se não tiver esse detalhe quando o horario de inico for maior, o resultado vai ser a quantidade de horas não jogadas e não, as jogadas.
