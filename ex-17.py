#17) Ler o ano atual e o ano de nascimento de uma pessoa. Escrever uma mensagem que diga se ela poderá ou não votar este ano (não é necessário considerar o mês em que a pessoa nasceu).
ano = int(input('Digite sua idade para saber se pode votar: '))
if ano <= 2009:
    print('Pode votar')
else:
    print('Não pode votar')

