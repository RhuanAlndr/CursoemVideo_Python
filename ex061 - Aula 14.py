pt = int(input('Qual é o primeiro termo da PA? '))
r = int(input('Qual é a razão da PA? '))
c = pt
while pt != c + 10 * r:
    print('{}'.format(pt), end=' - ')
    pt += r
print('Acabou!')
