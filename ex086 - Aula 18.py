m = []
d = []
for c in range(0, 3):
    for n in range(0, 3):
        d.append(int(input(f'Digite um valor para {c, n}: ')))
    m.append(d[:])
    d.clear()
for c in range(0, 3):
    for n in range(0, 3):
        print(f'[{m[c][n]:^5}]', end=' ')
    print()
