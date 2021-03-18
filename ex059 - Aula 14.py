p = False
n1 = float(input('Digite o 1º número: '))
n2 = float(input('Digite o 2º número: '))
while not p:
    print('Agora digite uma das opções:'
          '\n   [1] somar'
          '\n   [2] multiplicar'
          '\n   [3] maior'
          '\n   [4] novos números'
          '\n   [5] sair do programa')
    r = int(input('Sua escolha é: '))
    if r == 1:
        print('A soma entre {} + {} é {}.'.format(n1, n2, n1 + n2))
    elif r == 2:
        print('A multiplicação de {} x {} é {}.'. format(n1, n2, n1 * n2))
    elif r == 3:
        if n1 == n2:
            print('Não existe número maior, ambos são iguais.')
        else:
            if n1 > n2:
                m = n1
            elif n2 > n1:
                m = n2
            print('O maior número é {}.'.format(m))
    elif r == 4:
        n1 = float(input('Digite um número: '))
        n2 = float(input('Digite outro número: '))
    elif r == 5:
        p = True
    else:
        print('Opção inválida. Tente novamente')
    print(10 * '=-=')
