s = cmil = co = 0
while True:
    n = input('Nome do produto: ').title()
    p = float(input('Preço: R$'))
    r = 't'
    s += p
    co += 1
    if p > 1000:
        cmil += 1
    if co == 1 or p < pb:
        nb = n
        pb = p
    while r not in 'sn':
        r = input('Quer continuar? [S/N] ').lower()
    if r in 'n':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total da compra foi R${s:.2f}'
      f'\nTemos {cmil} produtos custando mais de R$1000.00'
      f'\nO produto mais barato foi {nb} que custa R${pb:.2f}')
