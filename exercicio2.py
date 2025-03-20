conta = int(input('Digite o número da sua conta: '))
saldo = float(input('Digite seu saldo: '))
debido = float(input('Digite seu débito: '))
credito = float(input('Digite seu Crédito: '))

saldo_atual = saldo - debido + credito

if saldo_atual >= 0:
    print(f'Saldo positivo, R${saldo_atual}')

else:
    print(f'Saldo negativo R${saldo_atual}')