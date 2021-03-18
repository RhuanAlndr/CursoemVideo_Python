print('Programa de Tabuada'
      '\nPara encerrar, digite um número negativo')
print('=-=' * 13)
while True:
    c = 0
    n = int(input('Qual tabuada você quer? '))
    if n < 0:
        break
    while c < 10:
        c += 1
        print(f'{n} x {c} = {n * c}')
    print('=-=' * 8)
print('Programa encerrado!')
