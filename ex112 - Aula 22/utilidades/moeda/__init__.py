def aumentar(n, a=0, f=False):
    na = n + n / 100 * a
    if f:
        na = moeda(na)
    return na


def diminuir(n, d=0, f=False):
    nd = n - n / 100 * d
    if f:
        nd = moeda(nd)
    return nd


def dobro(n, f=False):
    num = n * 2
    if f:
        num = moeda(num)
    return num


def metade(n, f=False):
    num = n / 2
    if f:
        num = moeda(num)
    return num


def moeda(v):
    p = f'R${v:.2f}'
    return p


def resumo(n, a, d):
    t = 'RESUMO DO VALOR'
    print('~' * 40)
    print(f'{t:^40}')
    print('~' * 40)
    print(f'{"Preço análisado:":<30} {moeda(n)}')
    print(f'{"Dobro do preço:":<30} {dobro(n, True):<30}')
    print(f'{"Metade do preço:":<30} {metade(n, True)}')
    print(f'{f"{n:.0f}% de aumento:":<30} {aumentar(n, a, f=True)}')
    print(f'{f"{n:.0f}% de redução:":<30} {diminuir(n, d, True)}')
    print('~' * 40)
