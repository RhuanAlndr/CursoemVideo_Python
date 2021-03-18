from time import sleep


def contagem(c, f, p):
    if p < 0:
        a = p * -1
    elif p == 0:
        a = 1
        p = 1
    else:
        a = p
    print(f'Contagem de {c} até {f} de {a} em {a}')
    if f < c and p < 0:
        p = p * -1
    if f < c:
        p = p * -1
        f = f - 1
    elif f > c and p < 0:
        f = f + 1
        p = p * -1
    else:
        f = f + 1
    for n in range(c, f, p):
        print(n, end=' ')
        sleep(0.75)
    print('FIM!')
    sleep(0.75)


contagem(1, 10, 1)
print('=' * 30)
contagem(10, 0, 2)
print('=' * 30)
print('Sua vez de personalizar a contagem!')
contagem(
    int(input('Início: ')),
    int(input('Fim: ')),
    int(input('Passo: '))
)
