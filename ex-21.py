hora_trabalhada = int(input('Digite as horas trabalhadas: '))
valor_hora = 6.42
valor_hora_extra = 6.42 * 1.5
hora_extra = (40 - hora_trabalhada)* valor_hora_extra
salario = (hora_trabalhada * valor_hora) + hora_extra
print(salario)
    
