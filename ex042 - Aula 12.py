r1 = float(input('Me dê uma reta: '))
r2 = float(input('Outra reta: '))
r3 = float(input('Agora uma última: '))
if r1 + r2 < r3 or r1 + r3 < r2 or r2 + r3 < r1:
    print('Essas retas não podem formar um triângulo!')
else:
    if r1 == r2 == r3:
        t = 'Equilátero'
    elif r1 == r2 or r1 == r3 or r2 == r3:
        t = 'Isósceles'
    else:
        t = 'Escaleno'
    print('Essas retas podem formar um triângulo {}.'.format(t))
