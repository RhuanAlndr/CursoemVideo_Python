def fatorial(n=0, show=False):
    """
    Calcula o Fatorial de um número
    :param n: O número a ser calculado
    :param show: (opcional) Mostrar ou não a conta
    :return: O valor do Fatorial de um número n
    """
    r = 1
    print(f'{n}', end=' ')
    for nu in range(n, 0, -1):
        r *= nu
        if show and nu != 1:
            print(f'X {nu - 1}', end=' ')
    print(f'= {r}')


fatorial(6)
