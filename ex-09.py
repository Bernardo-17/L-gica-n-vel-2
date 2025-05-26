#9) O custo de um carro novo ao consumidor é a soma do custo de fábrica com a porcentagem do distribuidor e dos impostos (aplicados ao custo de fábrica). Supondo que o percentual do distribuidor seja de 28% e os impostos de 45%, escrever um algoritmo para ler o custo de fábrica de um carro, calcular e escrever o custo final ao consumidor. 
carro_de_fabrica = int(input('Digite o valor do carro de fábrica: '))
print(f'O valor final do carro para o consumidor é de com os impostos de distribuidor e impostos:{carro_de_fabrica + (carro_de_fabrica * 0.45) + (carro_de_fabrica)*0.28} ')
