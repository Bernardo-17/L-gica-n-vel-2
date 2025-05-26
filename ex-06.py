6) Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias e escreva a idade dessa pessoa expressa apenas em dias. Considerar ano com 365 dias e mês com 30 dias.
anos = int(input('Digite sua idade: '))
meses = int(input('Digite o mês em que nasceu: '))
dias = int(input('Digite o dia em que nasceu: '))
print(f'Você tem {anos} anos, {meses} meses e {dias} dias ')
print(f'Sua idade em dias é {(anos * 365)+(meses * 30) }')
