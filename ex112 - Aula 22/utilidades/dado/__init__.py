def leiadinheiro(t):
    while True:
        p = input(f'{t}')
        nf = p.replace(',', '.', 1).strip()
        if nf.isnumeric():
            return float(nf)
        else:
            print(f'ERRO! "{p.strip()}" não é um número.')
