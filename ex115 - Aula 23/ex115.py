import defs

#banco de dados
arq = 'banco.txt'

while True:
    o = defs.menu()
    if o == 1:
        defs.verarq(arq)
        defs.verpessoas(arq)
    elif o == 2:
        defs.verarq(arq)
        d = defs.cadastro()
        defs.adicionar(d, arq)
    elif o == 3:
        break
