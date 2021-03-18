d = dict()
p = list()
t = 0
while True:
    d['nome'] = input('Nome: ')
    while True:
        d['sexo'] = input('Sexo: [M/F] ').upper()
        if d['sexo'] in 'MF':
            break
        print('ERRO! Digite apenas M ou F.')
    d['idade'] = int(input('Idade: '))
    t += d['idade']
    p.append(d.copy())
    while True:
        a = input('Quer continuar? [S/N] ').lower()
        if a in 'sn':
            break
        print('ERRO! Digite apenas S ou N.')
    if a in 'n':
        break
print(f'O grupo tem {len(p)} pessoas.'
      f'\nA média de idade é de {t / len(p):.0f}'
      f'\nAs mulheres cadastradas foram:', end=' ')
for c, v in enumerate(p):
    if p[c]['sexo'] == 'F':
        print(f'{p[c]["nome"]}', end=' ')
print('\nLista das pessoas que estão acima da média:')
for c, v in enumerate(p):
    if p[c]['idade'] > t / len(p):
        print(f'Nome = {p[c]["nome"]}; sexo = {p[c]["sexo"]}; idade = {p[c]["idade"]}')
