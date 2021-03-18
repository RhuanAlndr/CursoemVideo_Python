c = ('\33[0m',      # 0 - sem cor
     '\33[30;41m',  # 1 - vermelho
     '\33[30;42m',  # 2 - verde
     '\33[30;43m',  # 3 - amarelo
     '\33[30;44m',  # 4 - azul
     '\33[30;45m',  # 5 - roxo
     '\33[7m'       # 6 - branco
     )


def pyhelp(aju):
    titulo(f'Acessando manual do comando {aju}', 4)
    print(c[6], end='')
    help(aju)
    print(c[0], end='')


def titulo(tit, cor=0):
    tam = len(tit) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {tit}')
    print('~' * tam)
    print(c[0], end='')


while True:
    titulo('AJUDA DO PYHELP', 2)
    ajuda = (input('Função ou Biblioteca: ').lower())
    if ajuda.lower() == 'fim':
        break
    else:
        pyhelp(ajuda)

titulo('FIM! ATÉ LOGO!', 1)
