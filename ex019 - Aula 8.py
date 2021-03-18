from random import choice
print('Diga abaixo os nomes dos alunos:')
a = input('1: ')
b = input('2: ')
c = input('3: ')
d = input('4: ')
l = [a, b, c, d]
v = choice(l)
print('O aluno escolhido foi: {}'.format(v))
