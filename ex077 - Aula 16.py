l = 'APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS',\
    'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO'
for t in range(0, len(l)):
    print(f'\nNa palavra {l[t]} temos', end=' ')
    for c in l[t]:
        if c in 'AEIOU':
            print(c.lower(), end=' ')
