from random import randrange
na = (randrange(0, 10), randrange(0, 10), randrange(0, 10), randrange(0, 10), randrange(0, 10))
print(f'Os valores soteados foram:', end=' ')
for n in na:
    print(n, end=' ')
o = sorted(na)
print(f'\nO menor número é {min(na)} e o maior é {max(na)}')
