from datetime import date
s = 0
for c in range(0, 7):
    an = int(input('Em que ano a {}ª pessoa nasceu: '.format(c + 1)))
    i = date.today().year - an
    if i >= 21:
        s += 1
if s == 1:
    print('{} pessoa é maior de idade e {} não são maiores ainda.'.format(s, 7 - s))
elif s == 6:
    print('{} pessoas são maiores de idade e {} pessoa não é maior ainda.'.format(s, 7 - s))
else:
    print('{} pessoas são maiores de idade e {} não são maiores ainda.'.format(s, 7 - s))