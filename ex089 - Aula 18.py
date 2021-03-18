l = list()
a = list()
n = list()
while True:
    a.append(input('Nome: '))
    n.append(float(input('Nota 1: ')))
    n.append(float(input('Nota 2: ')))
    a.append(n[:])
    l.append(a[:])
    n.clear()
    a.clear()
    while True:
        r = input('Quer continuar? [S/N] ').lower()
        if r in 'sn':
            break
    if r in 'n':
        break
print('=' * 30)
print('Nº', f'{"NOME"}', f'{"MÉDIA":>20}')
print('=' * 30)
for c, e in enumerate(l):
    print(f'{c} {e[0]:<20} {(e[1][0] + e[1][1]) / 2:>2.1f}')
while True:
    cho = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if cho == 999:
        break
    print(f'As notas de {l[cho][0]} são {l[cho][1]}')
