from time import sleep
from random import randint
numbers = list()


def sorteia():
    print(f'Sorteando os valores da lista:', end=' ')
    for c in range(0, 5):
        sleep(0.5)
        n = randint(1, 10)
        numbers.append(n)
        print(f'{n}', end=' ')
    sleep(0.5)
    print()


def somaPar():
    s = 0
    for c in numbers:
        if c % 2 == 0:
            s += c
    print(f'A soma dos valores pares de {numbers} é: {s}')


sorteia()
somaPar()
