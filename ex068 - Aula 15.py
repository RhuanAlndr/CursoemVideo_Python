from random import randint
nv = 0
print('Vamos jogar PAR ou ÍMPAR?')
print('=-=' * 8)
while True:
    np = randint(0, 10)
    nj = int(input('Escolha um número: '))
    e = ' '
    while e not in 'ip':
        e = str(input('PAR ou ÍMPAR? [P/I] ')).lower().strip()
    s = nj + np
    if s % 2 == 0:
        r = 'p'
        re = 'PAR'
    else:
        r = 'i'
        re = 'ÍMPAR'
    print(f'Você jogou {nj} e o PC {np}. Total de {s} deu {re}')
    if e == r:
        print('VOCÊ GANHOU!')
    else:
        print('VOCÊ PERDEU!')
        break
    print('~' * 13)
    nv += 1
print('~' * 13)
print(f'GAME OVER! Você venceu {nv} vezes.')
