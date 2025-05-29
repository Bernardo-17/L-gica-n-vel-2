#24) Faça um algoritmo para ler: número da conta do cliente, saldo, débito e crédito. Após, calcular e escrever o saldo atual (saldo atual = saldo - débito + crédito). Também testar se saldo atual for maior ou igual a zero escrever a mensagem 'Saldo Positivo', senão escrever a mensagem 'Saldo Negativo'.
numero_da_conta = int(input('Digite o numero da sua conta: '))
saldo = float(input('Digite o saldo de sua conta: '))
debito = float(input('Digite o valor de seu debito: '))
credito = float(input('Digite o valor de seu credito: '))
saldo_atual = saldo - debito + credito
print(f'O seu saldo atual e de: R${saldo_atual}')
if saldo_atual > 0:
    print('Saldo Positivo')
else:
    print('Saldo Negativo')
