def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except KeyboardInterrupt:
            print('O usuário preferiu não digitar nenhum número.')
            return 0
        except Exception as erro:
            print(f'Desculpe! Erro {erro.__class__}')
        else:
            return n


def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except KeyboardInterrupt:
            print('O usuário preferiu não digitar nenhum número.')
            return 0
        except Exception as erro:
            print(f'Desculpe! erro {erro.__class__}')
        else:
            return n


ni = leiaint('Digite um número inteiro: ')
nf = leiafloat('Digite um número float: ')
print(f'O usuário digitou {ni} e {nf}')
