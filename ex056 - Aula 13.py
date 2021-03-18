m = 0 #média
nhmv = 0 #nome do homem mais velho
ih = 0 #idade do homem mais velho
mm = 0 #mulheres menos de vinte
for c in range(1, 5):
    n = input('Digite o nome da {}ª pessoa: '.format(c))
    i = int(input('Digite a idade da {}ª pessoa: '.format(c)))
    s = int(input('Digite 1 para escolher sexo masculino e 2 para feminino: '))
    m += i
    if c == 1 and s == 1:
        nhmv = n
        ih = i
    elif i > ih and s == 1:
        nhmv = n
        ih = i
    if s == 2 and i < 20:
        mm += 1
if nhmv == 0:
    print('A idade média do grupo é {}, não tem homem mais velho '
          'e tem {} mulheres com menos de 20 anos.'.format(m / 4, mm))
else:
    print('A idade média do grupo é {}, o nome do homem mais velho com {} anos é {} '
          'e tem {} mulheres com menos de 20 anos.'.format(m / 4, ih, nhmv, mm))
