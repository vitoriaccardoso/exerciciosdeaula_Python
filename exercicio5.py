valor1 = float(input('Digite um valor: '))

while True:
    valor2 = float(input('Digite um valor: '))
    if valor2 != 0:
        divisao = valor1 / valor2
        print(divisao)
        break
    else:
        
        print('Erro')
        outrovalor = float(input('Digite outro valor: '))
        resultado = valor1/outrovalor
        print(resultado)
    break
    

    

