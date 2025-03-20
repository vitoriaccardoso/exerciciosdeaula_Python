macas = int(input('Digite quantas maçãs você comprou: '))
if macas <= 12:
    soma = float(macas * 1.30)
    print(f'Você vai pagar R${soma:.2f}')

else:
    soma2 = int(macas * 1)
    print(f'Você vai pagar R${soma2}')

