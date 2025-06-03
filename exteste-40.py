#40) Faça um algoritmo para ler: a descrição do produto (nome), a quantidade adquirida e o preço unitário.
#  Calcular e escrever o total (total = quantidade adquirida * preço unitário), o desconto e o 
# total a pagar (total a pagar = total - desconto), sabendo-se que: 
#- Se quantidade <= 5 o desconto será de 2%
#- Se quantidade > 5 e quantidade <=10 o desconto será de 3%
#- Se quantidade > 10 o desconto será de 5%
nome_do_produto = input('Digite o nome do produto: ')
quantidade_adquirida = int(input('Digite a quantidade desejada do produto: '))
preço_unitário = float(input('Digite o preço do protudo: '))
desconto_de_2 = quantidade_adquirida * 0.02
desconto_de_3 = quantidade_adquirida * 0.03
total = quantidade_adquirida * preço_unitário
total_a_pagar_menor_5 = (quantidade_adquirida * preço_unitário) - desconto_de_2
total_a_pagar_maior_5_menor_10 = (quantidade_adquirida * preço_unitário) - desconto_de_3
if quantidade_adquirida <= 5:
    print(f'O produto {nome_do_produto}, quantidade de {quantidade_adquirida} e preço unitário de {preço_unitário}\nTotal: {total_a_pagar_menor_5}')

elif quantidade_adquirida >5 and <= 10:
#
    print(f'O produto {nome_do_produto}, quantidade de {quantidade_adquirida} e preço unitário de {preço_unitário}\nTotal: {total_a_pagar_maior_5_menor_10}')

else:
    print('Algo foi digitado incorretamente.')
