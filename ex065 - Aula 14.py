r = '0'
c = 0
s = 0
print('Você poderá digitar quantos números inteiros quiser!'
      '\nNo final verá o menor, o maior e a média dos números.'
      '\n\33[33mQuando quiser parar o programa digite 000\33[m')
while r != '000':
    n = int(input('Digite um número inteiro: '))
    r = str(input('\33[31mDeseja digitar outro número?\33[m '))
    c += 1
    s += n
    if c == 1:
        ma = n
        me = n
    else:
        if n > ma:
            ma = n
        if n < me:
            me = n
print('O menor número é {}'
      '\nO maior número é {}'
      '\nA média entre eles é {}'.format(me, ma, s / c))
