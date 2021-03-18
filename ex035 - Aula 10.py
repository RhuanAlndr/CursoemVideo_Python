r1 = float(input('Diga a medida de uma reta: '))
r2 = float(input('Diga a medida de outra reta: '))
r3 = float(input('Agora uma última reta: '))
if (r1 + r2) > r3 and (r1 + r3) > r2 and (r2 + r3) > r1:
    print('Essas retas podem formar um triângulo!')
else:
    print('Essas retas não podem formar um triângulo!')
