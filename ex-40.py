#40) Faça um algoritmo para ler: a descrição do produto (nome), a quantidade adquirida e o preço unitário.
#  Calcular e escrever o total (total = quantidade adquirida * preço unitário), o desconto e o 
# total a pagar (total a pagar = total - desconto), sabendo-se que: 
#- Se quantidade <= 5 o desconto será de 2%
#- Se quantidade > 5 e quantidade <=10 o desconto será de 3%
#- Se quantidade > 10 o desconto será de 5%
nome_do_produto = input('Digite o nome do produto: ')
quantidade_adquirida = int(input('Digite a quantidade desejada do produto: '))
preço_unitário = float(input('Digite o preço do protudo: R$'))
desconto_de_2 = quantidade_adquirida * preço_unitário * 0.02
desconto_de_3 = quantidade_adquirida * preço_unitário * 0.03
desconto_de_5 = quantidade_adquirida * preço_unitário * 0.05
total = quantidade_adquirida * preço_unitário
total_a_pagar_menor_5 = total - desconto_de_2
total_a_pagar_maior_5_menor_10 = total - desconto_de_3
total_a_pagar_maior_10 = total - desconto_de_5

if quantidade_adquirida <= 5:
    print(f'O produto {nome_do_produto}, quantidade de {quantidade_adquirida} e preço unitário de R${preço_unitário}\nTotal: R${total_a_pagar_menor_5:2f}')

elif quantidade_adquirida > 5 and quantidade_adquirida <= 10:
    print(f'O produto {nome_do_produto}, quantidade de {quantidade_adquirida} e preço unitário de R${preço_unitário}\nTotal: R${total_a_pagar_maior_5_menor_10:.2f}')

elif quantidade_adquirida > 10:
    print(f'O produto {nome_do_produto}, quantidade de {quantidade_adquirida} e preço unitário de R${preço_unitário}\nTotal: R${total_a_pagar_maior_10:.2f}')

else:
    print('Algo foi digitado incorretamente.')
