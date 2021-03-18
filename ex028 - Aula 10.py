from random import randint
n = randint(0, 5)
r = int(input('De 0 a 5 qual é o número que o computador pensou? '))
if n == r:
    print('Parabéns você acertou!')
else:
    print('Poxa não foi dessa vez que você conseguiu!')
