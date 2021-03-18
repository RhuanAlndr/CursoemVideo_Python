n = list()
while True:
    v = int(input('Digite um valor: '))
    if v not in n:
        n.append(v)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    while True:
        r = input('Quer continuar? [S/N] ').lower()
        if r in 'sn':
            break
    if r == 'n':
        break
n.sort()
print('=-=' * 10)
print(f'Você digitou os valores {n}')
