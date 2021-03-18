l = list()
while True:
    v = int(input('Digite um valor: '))
    l.append(v)
    while True:
        r = input('Quer continuar? [S/N] ').lower()
        if r in 'sn':
            break
    if r in 'n':
        break
lp = list()
li = list()
for c in range(0, len(l)):
    if l[c] % 2 == 0:
        lp.append(l[c])
    else:
        li.append(l[c])
print('=-=' * 20)
print(f'A lista completa é {l}')
co = len(lp)
if co == 0:
    print('Não foi digitado números pares.')
else:
    print(f'A lista de pares é {lp}')
co = len(li)
if co == 0:
    print('Não foi digitado números ímpares.')
else:
    print(f'A lista de ímpares é {li}')
