tm = th = tmm = 0
while True:
    s = 't'
    e = 't'
    print('CADASTRE UMA PESSOA')
    print('=' * 19)
    i = int(input('Idade: '))
    while s not in 'fm':
        s = input('Sexo: [MF] ').lower().strip()
    if i >= 18:
        tm += 1
    if s in 'm':
        th += 1
    if s in 'f' and i < 20:
        tmm += 1
    while e not in 'sn':
        e = input('Quer continuar? [S/N] ').lower()
    print('=' * 23)
    if e in 'n':
        break
print(f'Total de pessoas com mais de 18 anos: {tm}'
      f'\nAo todo temos {th} homens cadastrados'
      f'\nE temos {tmm} com menos de 20 anos.')
