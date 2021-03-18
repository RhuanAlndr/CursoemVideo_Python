from random import randint
from time import sleep
from operator import itemgetter
'''p = dict()
l = list()
ls = list()
print('Valores sorteados:')
for j in range(0, 4):
    p['Jogador'] = j + 1
    p['Jogada'] = randint(1, 6)
    l.append(p.copy())
    print(f'    O jogador {l[j]["Jogador"]} tirou {l[j]["Jogada"]}')
    sleep(0.75)
print('Ranking dos jogadores')
atu = 0
cont = 0
for en in l:
    mai = 0
    for num, list in enumerate(l):
        if cont == 0 and l[num]['Jogada'] > mai or atu > l[num]['Jogada'] > mai:
            mai = l[num]['Jogada']
    for num, lis in enumerate(l):
        if mai == l[num]['Jogada']:
            ls.append(l[num])
            atu = l[num]['Jogada']
    cont += 1
for nume, lu in enumerate(ls):
    sleep(0.75)
    print(f'    {nume + 1}º lugar: Jogador {ls[nume]["Jogador"]} com {ls[nume]["Jogada"]}')'''

#solução mais simples
j = dict()
r = dict()
print('Valores sorteados:')
for n in range(1, 5):
    j[f'Jogador {n}'] = randint(1, 6)
for nj, v in j.items():
    print(f'    {nj} tirou {v} no dado.')
    sleep(.75)
r = sorted(j.items(), key=itemgetter(1), reverse=True)
print('Ranking dos jogadores')
for nr, d in enumerate(r):
    sleep(.75)
    print(f'    {r[nr][0]} tirou {r[nr][1]} no dado.')
