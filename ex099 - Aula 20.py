from time import sleep


def maior(*val):
    d = mai = 0
    print('Analisando os valores passados...')
    for c in val:
        sleep(0.75)
        print(c, end=' ')
        if d == 0 or c > mai:
            mai = c
            d = 1
    print(f'Foram analisados {len(val)} valores ao todo.'
          f'\nO maior valor informado foi {mai}')
    print('=' * 50)


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
