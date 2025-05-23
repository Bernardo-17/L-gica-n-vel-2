Votos_brancos = int(input('Qual a quantidade de votos brancos: '))
Votos_nulos = int(input('Qual a quantidade de votos nulos: '))
Votos_validos = int(input('Qual a quantidade de votos validos: '))
Votos_totais = Votos_brancos + Votos_nulos + Votos_validos
print(f'Total de votos é {Votos_totais}!')
print(f'Votos brancos tem a porcentagem de {Votos_brancos/Votos_totais*100:.1f}%.')
print(f'Votos nulos tem a porcentegem de {Votos_nulos/Votos_totais*100:.1f}%.')
print(f'Votos validos tem a porcentagem de {Votos_validos/Votos_totais*100:.1f}%.')
