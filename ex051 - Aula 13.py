r = int(input('Qual a razão da PA? '))
pt = int(input('Qual o primeiro termo da PA? '))
print('Os 10 primeiros termos dessa progressão são:')
for c in range(pt, pt + 9 * r + 1, r):
    print(c, end=' - ')
print('Acabou')
