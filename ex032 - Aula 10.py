from datetime import date
a = int(input('Digite um ano, para ano atual digite 0: '))
if a == 0:
    a = date.today().year
r1 = a % 4
r2 = a % 100
r3 = a % 400
if r1 == 0 and r2 != 0 or r3 == 0:
    print('O ano {} é bissexto!'.format(a))
else:
    print('O ano {} não é bissexto!'.format(a))
