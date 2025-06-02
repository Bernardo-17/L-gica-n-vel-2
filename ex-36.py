#36) Escreva um algoritmo que leia as idades de 2 homens e de 2 mulheres 
# (considere que as idades dos homens serão sempre diferentes entre si, bem como as das mulheres). 
# Calcule e escreva a soma das idades do homem mais velho com a mulher mais 
# nova, e a soma das idades do homem mais novo com a mulher mais velha.
mulherN = int(input('Digite a idade da mulher mais nova: '))
mulherV = int(input('Digite a idade da mulher mais velha: '))
homemN = int(input('Digite a idade do homem mais novo: '))
homemV = int(input('Digite a idade do homem mais velho: '))
if homemV > homemN and mulherV > mulherN:
    print(f'A soma das idade do homem mais velho e a mulher mais nova é: {homemV} + {mulherN} = {homemV + mulherN}.\nA soma do homem mais novo com a mulher mais velha é: {homemN} + {mulherV} = {homemN + mulherV}.')
else:
    print('Algo foi digitado incorretamente.')
