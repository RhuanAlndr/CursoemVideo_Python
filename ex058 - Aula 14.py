from random import randint
r = 0
nt = 0
n = randint(1, 10)
print('O PC vai pensou em um número de 1 a 10.'
      '\nTENTE ADIVINHAR!')
while not r == n:
    if r != 0:
        if n > r:
            print('Uuumm o número é maior...')
        else:
            print('Uuumm o número é menor...')
    r = int(input('Qual é o número que o pc pensou? '))
    nt += 1
print('\33[34mVOCÊ VENCEU!\33[m E precisou de {} tentativas'.format(nt))
