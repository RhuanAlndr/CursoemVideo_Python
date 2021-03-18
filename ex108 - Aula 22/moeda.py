def aumentar(n, a=0):
    na = n + n / 100 * a
    return na


def diminuir(n, d=0):
    nd = n - n / 100 * d
    return nd


def dobro(n):
    num = n * 2
    return num


def metade(n):
    num = n / 2
    return num


def moeda(v):
    p = str(f'R${v:.2f}')
    return p.replace('.', ',')
