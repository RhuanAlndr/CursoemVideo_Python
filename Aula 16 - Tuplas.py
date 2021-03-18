lanche = 'lasanha', 'hambúrguer', 'pizza'
#tuplas são imutáveis
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}')

for pos, food in enumerate(lanche):
    print(f'Eu vou comer {food} na posição {pos}')
print('Comi pra caramba!')

#sorted colocar em ordem
print(sorted(lanche))
