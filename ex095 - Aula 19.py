d = dict()
gp = list()
j = list()
t = 0
while True:
    d['nome'] = input('Nome do Jogador: ')
    n = int(input(f'Quantas partidas {d["nome"]} jogou? '))
    for c in range(0, n):
        gp.append(int(input(f'Quantos gols na {c + 1}ª partida? ')))
    d['gols'] = gp[:]
    d['total'] = sum(gp)
    gp.clear()
    j.append(d.copy())
    while True:
        a = input('Quer continuar? [S/N] ').lower()
        if a in 'sn':
            break
        print('ERRO! Por favor, digite apenas S ou N.')
    print('=' * 45)
    if a in 'n':
        break
print(f'Cod {"Nome":<15} {"Gols":<15} {"Total":<}')
print('=' * 45)
for cod, jo in enumerate(j):
    print(f'{cod:<4}{j[cod]["nome"]:<15} {str(j[cod]["gols"]):<15} {str(j[cod]["total"]):<15}')
print('=' * 45)
while True:
    an = int(input('Mostrar dados de qual jogador? '))
    if an == 999:
        print('=' * 45)
        print('<< VOLTE SEMPRE >>')
        break
    if an <= len(j) - 1:
        print(f'== LEVANTAMENTO DO JOGADOR {(j[an]["nome"]).upper()}:')
        for cont, par in enumerate(j[an]['gols']):
            print(f'   Na {cont + 1}ª partida, fez {par} gols.')
    else:
        print(f'OPS! Não pudemos encontrar o jogador com código {an}! Tente novamente.')
    print('=' * 45)
