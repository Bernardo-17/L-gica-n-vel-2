#6) Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias e escreva a idade dessa pessoa expressa apenas em dias. Considerar ano com 365 dias e mês com 30 dias.
anos = int(input('Digite sua idade: '))
meses = int(input('Digite o mês em que nasceu: '))
print(f'Sua idade é {(anos * 365)+(meses * 30)}')
