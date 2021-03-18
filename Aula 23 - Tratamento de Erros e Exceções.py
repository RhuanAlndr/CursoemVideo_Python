try:
    a = int(input('Digite um número: '))
    b = int(input('digte um número: '))
    d = a / b
except (ValueError, TypeError):
    print('oi')
except KeyboardInterrupt:
    print('Key')
