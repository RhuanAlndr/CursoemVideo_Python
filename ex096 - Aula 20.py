def area(l, c):
    a = l * c
    print(f'A área de um terreno {l} X {c} é de {a}m².')


print('CONTROLE DE TERRENO')
print('=' * 20)
area(
    float(input('LARGURA (m): ')),
    float(input('COMPRIMENTO (m): '))
)
