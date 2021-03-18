l = list()
for c in range(0, 5):
    v = int(input('Digite um valor: '))
    p = 0
    while True:
        if c == 0 or p == len(l):
            l.append(v)
            print(f'Adicionado ao final da lista...')
            break
        if v < l[p]:
            l.insert(p, v)
            print(f'Adicionado na posição {p} da lista...')
            break
        p += 1
print(f'Os valores digitados em ordem foram {l}')
