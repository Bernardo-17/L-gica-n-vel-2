combustivel = input('Digite o combustivel: ' )
if combustivel == "gasolina" or 'Gasolina':
    combustivel = int(input('Digite a quantidade de Litros desejados: '))
    if combustivel <= 20:
        print(f'O valor de: R${combustivel * 2.90 - ((combustivel * 2.90) * 0.04):.2f} ')
    elif combustivel >= 20:
        print(f'O valor de: R${combustivel * 2.90 - ((combustivel * 2.90)* 0.06):.2f} ')
elif combustivel == "alcool" or 'Álcool' or 'álcool':
    combustivel = int(input('Digite a quantidade de Litros desejados: '))
    if combustivel <= 20:
        print(f'O valor de: R${combustivel * 3.30 - ((combustivel * 3.30) * 0.03):.2f} ')
    elif combustivel >= 20:
        print(f'O valor de: R${combustivel * 3.30 - ((combustivel * 3.30) * 0.05):.2f} ')
else:
    print('Valor não compreendido')
