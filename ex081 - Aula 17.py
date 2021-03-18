l = list()
while True:
    l.append(int(input('Digite um valor: ')))
    while True:
        r = input('Quer continuar? [S/N] ').lower()
        if r in 'sn':
            break
    if r in 'n':
        break
l.sort(reverse=True)
print(f'Você digitou {len(l)} elementos.'
      f'\nOs valores em ordem decrescente são {l}')
if 5 in l:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')
