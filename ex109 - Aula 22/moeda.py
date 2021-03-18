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
    p = str(f'R${v:.2f}')
    return p.replace('.', ',')
