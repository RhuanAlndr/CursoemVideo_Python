l = [[], []]
for c in range(1, 8):
    n = int(input(f'Digite o {c}º valor: '))
    if n % 2 == 0:
        l[0].append(n)
    else:
        l[1].append(n)
l[0].sort()
l[1].sort()
print(f'Os valores pares digitados foram: {l[0]}'
      f'\nOs valores ímpares digitados foram: {l[1]}')
