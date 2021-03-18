from random import randint
from time import sleep
n = list()
print('=' * 40)
print(f'{"JOGA NA MEGA SENA":^40}')
print('=' * 40)
j = int(input('Quantos jogos você quer que eu sorteie? '))
f = f' SORTEANDO {j} JOGOS '
print(f'{f:=^40}')
for r in range(1, j + 1):
    while True:
        v = randint(1, 61)
        if v not in n:
            n.append(v)
        if len(n) == 8:
            n.sort()
            break
    sleep(0.75)
    print(f'Jogo {r}: {n}')
    n.clear()
print(f'{" BOA SORTE! ":=^40}')
