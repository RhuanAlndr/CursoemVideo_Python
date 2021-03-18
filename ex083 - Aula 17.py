e = input('Digite uma expressão: ')
p = pf = 0
a = 'Expressão válida!'
while True:
    cp = 0
    if '(' in e[pf:]:
        p = e.index('(', pf)
    elif ')' in e[pf + 1:] or e[0] in ')':
        print('Expressão inválida!')
        break
    else:
        print(a)
        break
    if ')' in e[pf + 1:]:
        pf = e.index(')', pf + 1)
    else:
        print('Expressão inválida')
        break
    while True:
        if '(' in e[p + 1:pf]:
            p = e.index('(', p + 1, pf)
            if ')' in e[pf + 1:]:
                pf = e.index(')', pf + 1)
            else:
                print('Expressão inválida!')
                cp = 1
                break
        else:
            break
    if cp == 1:
        break
