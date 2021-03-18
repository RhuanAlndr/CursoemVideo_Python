l = (int(input('Digite um número: ')),
     int(input('Digite outro número: ')),
     int(input('Digite mais um número: ')),
     int(input('Digite um último número: ')))
print(f'Você digitou os valores {l}')
if 9 in l:
    print(f'Você digitou o valor 9 por {l.count(9)} vezes.')
else:
    print('Você não digitou o valor 9 nenhuma vez.')
if 3 not in l:
    print('Você não digtou o valor 3 nenhuma vez.')
else:
    print(f'O valor 3 aparece na posição {l.index(3) + 1}')
lp = ()
for c in range(0, 4):
    r = l[c] % 2
    if r == 0:
        ln = (l[c],)
        lp += ln
if lp == ():
    print('Não tem números pares')
else:
    print(f'Os números pares são {lp[0:]}')
