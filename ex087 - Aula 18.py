m = []
d = []
svp = sv3 = mv2 = 0
for l in range(0, 3):
    for c in range(0, 3):
        d.append(int(input(f'Digite um valor para {l, c}: ')))
    m.append(d[:])
    d.clear()
for l in range(0, 3):
    sv3 += m[l][2]
    if m[1][l] > mv2:
        mv2 = m[1][l]
    for c in range(0, 3):
        if m[l][c] % 2 == 0:
            svp += m[l][c]
        print(f'[{m[l][c]:^5}]', end=' ')
    print()
print(f'A soma de todos os valores pares é: {svp}'
      f'\nA soma dos valores da terceira coluna é: {sv3}'
      f'\nO maior valor da segunda linha é: {mv2}')
