from math import radians, cos, sin, tan
a = float(input('Me de um ângulo: '))
s = sin(radians(a))
c = cos(radians(a))
t = tan(radians(a))
print('O seno de {} é {:.2f}'.format(a, s))
print('O cosseno de {} é {:.2f}'.format(a, c))
print('A tangente de {} é {:.2f}'.format(a, t))
