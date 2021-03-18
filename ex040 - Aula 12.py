n1 = float(input('Qual sua primeira nota? '))
n2 = float(input('Qual sua segunta nota? '))
m = (n1 + n2) / 2
print('Sua média foi {:.1f}, e você está'.format(m), end=' ')
if m < 5:
    print('\33[31mreprovado!\33[m')
elif m >= 7:
    print('\33[36maprovado!\33[m'.format(m))
else:
    print('de \33[33mrecuperação!\33[m'.format(m))
