# Example 1
'''def plus(a, b):
    s = a + b
    print(f'A soma de {a} e {b} é {s}.')


# Programa principal
plus(2, 3)
plus(5, 6)'''

# Example 2
'''def contador(*num):
    print(num)


contador(2, 1, 3, 4)
contador(4)'''

# Example 3
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [6, 5, 8, 2, 7, 9, 4, 1]
dobra(valores)
print(valores)
