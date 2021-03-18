v = list()
pma = list()
pme = list()
for n in range(0, 5):
    v.append(int(input(f'Digite um número para a posição {n}: ')))
print(f'Você digitou os valores: {v}')
me = v[0]
ma = v[0]
for c in range(0, 5):
    if v[c] < me:
        me = v[c]
    if v[c] > ma:
        ma = v[c]
pma = v.index(ma)
print(f'O maior valor digitado foi {ma} nas posições', end=' ')
while True:
    print(pma, end='...')
    if ma in v[pma + 1:]:
        pma = v.index(ma, pma + 1)
    else:
        break
pme = v.index(me)
print(f'\nO menor valor digitado foi {me} nas posições', end=' ')
while True:
    print(pme, end='...')
    if me in v[pme + 1:]:
        pme = v.index(me, pme + 1)
    else:
        break
