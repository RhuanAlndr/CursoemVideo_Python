s = '0'
while s not in "mf":
    s = input('Qual é o seu sexo? [M/F]: ').lower().strip()
    if s not in 'mf':
        print('Por favor, digite apenas M ou F!')
if s == 'm':
    ss = ('masculino')
elif s == 'f':
    ss = ('feminino')
print('O sexo é {}!'.format(ss))
