def fatorial(n):
    f = 1
    for c in range(1, n+1):
        f *= c
    return f


com = int(input('Digite um número: '))
print(fatorial(com))
