while True:
    try:
        n1 = int(input('digite um número: '))
        n2 = int(input('digite outro numero:'))
        conta = n1 / n2

    except ZeroDivisionError:
        print('NÃO PERMITIDO POR 0, REFAÇA O CALCULO!')
    except ValueError:
        print('por favor, faça a conta digitando apenas numeros inteiros. ')

    else:
        print(f'{n1} dividido por {n2} é = {conta}')
    

