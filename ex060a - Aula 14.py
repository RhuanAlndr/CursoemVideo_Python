n = int(input('Digite um número que deseja fatorar: '))
c = n
f = 1
while c > 0:
    f *= c
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    c -= 1
print(f)
