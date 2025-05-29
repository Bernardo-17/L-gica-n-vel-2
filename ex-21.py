#21) A jornada de trabalho semanal de um funcionário é de 40 horas. O funcionário que trabalhar mais de 40 horas receberá hora extra, cujo cálculo é o valor da hora regular com um acréscimo de 50%. Escreva um algoritmo que leia o número de horas trabalhadas em um mês, o salário por hora e escreva o salário total do funcionário, que deverá ser acrescido das horas extras, caso tenham sido trabalhadas (considere que o mês possua 4 semanas exatas).
hora_trabalhada = int(input('Digite as horas trabalhadas em um mes: '))
valor_hora = float(input('Digite seu salario por hora: '))
valor_hora_extra = valor_hora * 1.5
hora_extra = (hora_trabalhada - 160) * valor_hora_extra
salario = (hora_trabalhada * valor_hora) + hora_extra
print(f'ganha: R${salario}')
    
