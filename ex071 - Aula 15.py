from math import floor
print('=' * 30)
print(str('BANCO RHUAN ALNDR').center(30))
print('=' * 30)
v = int(input('Que valor você quer sacar? R$'))
while True:
    c50 = v / 50
    c50 = floor(c50)
    v = v % 50
    print(f'Total de {c50} cédulas de R$50')
    if v == 0:
        break
    c20 = v / 20
    c20 = floor(c20)
    v = v % 20
    print(f'Total de {c20} cédulas de R$20')
    if v == 0:
        break
    c10 = v / 10
    v = v % 10
    c10 = floor(c20)
    print(f'Total de {c10} cédulas de R$10')
    if v == 0:
        break
    c1 = v / 1
    print(f'Total de {c1:.0f} cédulas de R$1')
    break
