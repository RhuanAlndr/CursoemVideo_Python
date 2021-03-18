n = int(input('Digite um número: '))
print('Digite \33[32m1 para converter em binário;\33[m '
               '\33[36m2 para octal;\33[m '
               '\33[31m3 para hexadecimal:\33[m ')
bc = int(input('Sua escolha: '))
if bc == 1:
    print('Esse número em binário é {}'.format(bin(n)[2:]))
elif bc == 2:
    print('Esse número em octal é {}'.format(oct(n)[2:]))
elif bc == 3:
    print('Esse número convertido em hexadecimal é {}'.format(hex(n)[2:]))
else:
    print('TENTE NOVAMENTE!')