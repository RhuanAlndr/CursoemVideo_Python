print('Sequência de Fibonacci')
nt = int(input('Quantos termos você quer mostrar? '))
n = 0
atual = 0
anterior = 1
c = 0
while c < nt:
    print(n, end=' - ')
    c += 1
    atual = anterior
    anterior = n
    n += atual
print('FIM')
