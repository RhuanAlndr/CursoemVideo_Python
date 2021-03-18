pt = int(input('Qual é o primeiro termo da PA? '))
r = int(input('Qual é a razão da PA? '))
c = 1
q = 1
t = 10
while q != 0:
    while c <= t:
        c += 1
        print(pt, end=' - ' if c <= t else '\n')
        pt += r
    print('Acabou!')
    q = int(input('Quantos termos você quer mostrar? '))
    t += q
print('Progressão finalizada com {} termos mostrados.'.format(c - 1))
