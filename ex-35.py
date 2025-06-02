#35) Um posto está vendendo combustíveis com a seguinte tabela de descontos: 
#Escreva um algoritmo que leia o número de litros vendidos e o 
#tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o 
#valor a ser pago pelo cliente sabendo-se que o preço do litro 
#da gasolina é R$ 3,30 e o preço do litro do álcool é R$ 2,90. 
tipo_combustivel = input('Digite o combustivel: ' )
Valor_litragem_gasolina = 2.90
Valor_litragem_álcool = 3.30
Valor_desconto_gasolina_menor_20 = 0.04
Valor_desconto_gasolina_maior_20 = 0.06
desconto_álcool_menor_20 = 0.03
desconto_álcool_maior_20 = 0.05

if tipo_combustivel =='Gasolina':
    quantidade_combustivel = float(input(f'Digite a quantidade de litros desejados de gasolina: '))
    if quantidade_combustivel <= 20:
        print(f'A gasolina fica no valor de: R${quantidade_combustivel * Valor_litragem_gasolina - ((quantidade_combustivel * Valor_litragem_gasolina) * Valor_desconto_gasolina_menor_20):.2f} ')
    elif quantidade_combustivel > 20:
        print(f'A gasolina fica no valor de: R${quantidade_combustivel * Valor_litragem_gasolina - ((quantidade_combustivel * Valor_litragem_gasolina)* Valor_desconto_gasolina_maior_20):.2f} ')
elif tipo_combustivel =='Álcool':
    quantidade_combustivel = float(input(f'Digite a quantidade de litros desejados de álcool: '))
    if quantidade_combustivel <= 20:
        print(f'O álcool fica no valor de: R${quantidade_combustivel * Valor_litragem_álcool - ((quantidade_combustivel * Valor_litragem_álcool) * desconto_álcool_menor_20):.2f} ')
    elif quantidade_combustivel > 20:
        print(f'O álcool fica no valor de: R${quantidade_combustivel* Valor_litragem_álcool - ((quantidade_combustivel * Valor_litragem_álcool) * desconto_álcool_maior_20):.2f} ')
else:
    print('Algo foi digitado incorretamente.')
