km = float(input('Quantos quilometros você percorreu? '))
d = int(input('Quantos dias você usou o carro? '))
a = km * 0.15 + 60 * d
print('O valor do aluguel vai ficar em R$ {:.2f}.'.format(a))
