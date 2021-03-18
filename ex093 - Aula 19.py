d = dict()
p = list()
t = 0
d['nome'] = input('Nome do Jogador: ')
n = int(input(f'Quantas partidas {d["nome"]} jogou? '))
for c in range(0, n):
    p.append(int(input(f'Quantos gols na {c + 1}ª partida? ')))
d['gols'] = p[:]
d['total'] = sum(p)
print('=' * 30)
for h, v in d.items():
    print(f'O campo {h.title()} tem o valor {v}.')
print('=' * 30)
print(f'O jogador {d["nome"]} jogou {len(d["gols"])} partidas.')
for cont, par in enumerate(d['gols']):
    print(f'Na {cont + 1}ª partida, fez {par} gols.')
print(f'Foi um total de {d["total"]} gols.')
