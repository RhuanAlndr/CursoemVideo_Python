from math import hypot
ca = float(input('Digite cateto adjace:'))
co = float(input('Digite cateto oposto:'))
h = hypot(ca, co)
print('A resposta é: {:.2f}'.format(h))
