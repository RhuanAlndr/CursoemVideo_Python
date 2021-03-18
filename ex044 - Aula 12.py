v = float(input('Qual o valor do produto? R$'))
fp = int(input('Digite para 1 para pagar à vista no dinheiro ou cheque'
               '\nOu digite 2 para pagar no cartão: '))
if fp == 1:
    vf = v - (v / 100 * 10)
else:
    d = int(input('Em quantas vezes você quer dividir? '))
    if d == 1:
        vf = v - (v / 100 * 5)
    elif d == 2:
        vf = v
    else:
        vf = v + (v / 100 * 20)
print('O valor do produto sairá por R${:.2f}'.format(vf))
