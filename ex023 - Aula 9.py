n = int(input('Digite um número de 0 a 9999: '))
nq = str(('{:4.0f}'.format(n)))
nc = nq.replace(' ', '0')
print('unidade: {}'.format(nc[-1]))
print('dezena: {}'.format(nc[-2]))
print('centena: {}'.format(nc[-3]))
print('milhar: {}'.format(nc[-4]))
