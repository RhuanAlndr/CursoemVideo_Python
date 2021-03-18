n = 0
c = 0
s = 0
print('Digite números que serão somados no final. '
      'Se quiser parar digite 999.')
while n != 999:
    s += n
    c += 1
    n = int(input('Digite um número inteiro: '))
print('Você digitou {} números e a soma entre eles é {}.'.format(c - 1, s))
