n = int(input('Digite um número que deseja fatorar: '))
r = n
for c in range(1, n):
    r = r * c
print('O número {} fatorado é {}!'.format(n, r))
