n = input('Diga seu nome: ').strip()
print('Primeiro nome: {}'.format(n.split()[0].title()))
print('Segundo nome: {}'.format(n.split()[-1].title()))
