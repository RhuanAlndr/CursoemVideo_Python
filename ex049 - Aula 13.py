n = int(input('Qual número você quer a tabuada? '))
print('A tabuada do {} é:'.format(n))
for t in range(1, 11):
    print('{} x {} = {}'.format(n, t, n * t))
