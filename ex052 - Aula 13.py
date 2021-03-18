n = int(input('Digite um número inteiro: '))
a = 0
for c in range(1, n + 1):
    if n % c == 0:
        a += 1
if a == 2:
    print('O número {} é primo!'.format(n))
else:
    print('O número {} não é primo!'.format(n))
