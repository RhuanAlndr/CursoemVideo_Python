from random import shuffle
print('Diga o nome dos alunos:')
a = input('1: ')
b = input('2: ')
c = input('3: ')
d = input('4: ')
l = [a, b, c, d]
shuffle(l)
print('a sequência é: {}'.format(l))
