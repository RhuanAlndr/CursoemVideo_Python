f = input('Escreva uma frase para saber se é um palindromo: ').strip().upper()
fa = f.replace(' ', '')
ff = (fa[::-1])
fi = ''
for c in range(len(fa) - 1, -1, -1):
    fi += fa[c]
if fi == fa:
    print('A frase é um palíndromo!')
else:
    print('A frase não é um palíndromo')
if fa == ff:
    print('Essa frase é um palíndromo!')
else:
    print('Essa frase não é um palíndromo!')
f2 = input('diga algo: ').split()
ff2 = ''.join(f2)
print(ff2)

