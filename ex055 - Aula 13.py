ma = 0
me = 0
for pp in range(1, 4):
    p = float(input('Quanto a {}ª pessoa pesa? '.format(pp)))
    if pp == 1:
        ma += p
        me += p
    else:
        if p > ma:
            ma = p
        if p < me:
            me = p
print('A pessoa mais pesada está com {:.2f} Kg'
      'e a mais leve está com {:.2f} Kg'.format(ma, me))
