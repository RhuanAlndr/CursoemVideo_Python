def leiaint(v):
    while True:
        if v.isnumeric():
            break
        else:
            print('\33[1;3;4;31mERRO! Digite um número inteiro válido.\33[m')
            v = input('Digite um número: ')
    return v


n = leiaint(input('Digite um número: '))
print(f'Você digitou o número {n}')
