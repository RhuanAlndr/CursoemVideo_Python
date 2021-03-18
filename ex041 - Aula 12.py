from datetime import date
an = int(input('Em que ano você nasceu? '))
i = date.today().year - an
if i <= 9:
    c = 'MIRIM'
elif i <= 14:
    c = 'INFANTIL'
elif i <= 19:
    c = 'JUNIOR'
elif i <= 25:
    c = 'SÊNIOR'
else:
    c = 'MASTER'
print('Você tem {} anos e está na categoria \33[34m{}\33[m'.format(i, c))
