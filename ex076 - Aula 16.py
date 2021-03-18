p = 'Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00,\
    'Tranferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32,\
    'Canetas', 22.30, 'Livro', 34.90
print('=' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('=' * 40)
for c in range(0, len(p), 2):
    print(f'{p[c]:.<30} R${p[c+1]:7.2f}')
print('=' * 40)
