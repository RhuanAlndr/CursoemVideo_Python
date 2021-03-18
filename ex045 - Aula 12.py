from random import randint
i = ('pedra', 'papel', 'tesoura')
j = int(input('Digite 0 para pedra \n       1 para papel \n       2 para tesoura'
              '\nSua escolha: '))
# p = choice([1, 2, 3])
p = randint(0, 2)
print('{} {}'.format(i[j],i[p]))
if p == 0:
    n = 'pedra'
elif p == 1:
    n = 'papel'
else:
    n = 'tesoura'
if p == j:
    print('O computador escolheu {}, deu empate.'.format(n))
elif j == 0 and p == 2 or j == 1 and p == 0 or j == 2 and p == 1:
    print('O computador escolheu {} e você ganhou!'.format(n))
else:
    print('O computador escolheu {} e você perdeu!'.format(n))
print('='*44)