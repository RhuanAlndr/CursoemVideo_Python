s = c = 0
print('Digite 999 para parar!')
while True:
    n = int(input('Digite um valor: '))
    if n == 999:
        break
    c += 1
    s += n
print(f'Você digitou {c} e a soma deles é {s}.')
