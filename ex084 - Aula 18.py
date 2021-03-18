l = list()
data = list()
pmai = pmen = 0
while True:
    data.append(str(input('Nome: ')))
    data.append(float(input('Peso: ')))
    l.append(data[:])
    if pmai == 0 or data[1] > pmai:
        pmai = data[1]
    if pmen == 0 or data[1] < pmen:
        pmen = data[1]
    data.clear()
    while True:
        r = input('Quer continuar? [S/N] ').lower()
        if r in 'sn':
            break
    if r in 'n':
        break
print(f'Você cadastrou {len(l)} pessoas.'
      f'\nO maior peso foi de {pmai}. Peso de', end=' ')
for p in l:
    if p[1] == pmai:
        print(f'[{p[0]}]', end=' ')
print(f'\nO menor peso foi de {pmen}. Peso de', end=' ')
for p in l:
    if p[1] == pmen:
        print(f'[{p[0]}]', end=' ')
