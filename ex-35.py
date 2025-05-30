#35) Um posto está vendendo combustíveis com a seguinte tabela de descontos: 
#Escreva um algoritmo que leia o número de litros vendidos e o 
#tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o 
#valor a ser pago pelo cliente sabendo-se que o preço do litro 
#da gasolina é R$ 3,30 e o preço do litro do álcool é R$ 2,90. 
tipo_combustivel = input('Digite o combustivel: ' )
if tipo_combustivel =='Gasolina':
    combustivel = int(input(f'Digite a quantidade de Litros desejados de {tipo_combustivel}: '))
    if combustivel <= 20:
        print(f'O valor de: R${combustivel * 2.90 - ((combustivel * 2.90) * 0.04):.2f} ')
    elif combustivel > 20:
        print(f'O valor de: R${combustivel * 2.90 - ((combustivel * 2.90)* 0.06):.2f} ')
elif tipo_combustivel =='Álcool':
    combustivel = int(input(f'Digite a quantidade de Litros desejados {tipo_combustivel}: '))
    if combustivel <= 20:
        print(f'O valor de: R${combustivel * 3.30 - ((combustivel * 3.30) * 0.03):.2f} ')
    elif combustivel > 20:
        print(f'O valor de: R${combustivel * 3.30 - ((combustivel * 3.30) * 0.05):.2f} ')
else:
    print('Algo foi digitado incorretamente')
