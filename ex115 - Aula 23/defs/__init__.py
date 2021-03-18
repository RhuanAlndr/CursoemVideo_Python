def menu():
    title('menu principal')
    print('1 - Ver pessoas cadastradas')
    print('2 - Cadastrar nova pessoa')
    print('3 - Sair do Sistema')
    print('=' * 35)
    try:
        o = int(input('Sua opção: '))
    except:
        print('\33[31;1mErro! Favor digitar uma opção válida!\33[m')
    else:
        return o


def verpessoas(f):
    title('pessoas cadastradas')
    a = open(f, 'rt')
    try:
        for c in a:
            c = c.replace('\n', '')
            print(f'{c.split(";")[0]:<20}{c.split(";")[1]:>10} anos')
    except:
        'não funcionou'
    a.close()


def cadastro():
    title('novo cadastro')
    n = input('Nome: ')
    while True:
        try:
            i = str(int(input('Idade: ')))
        except:
            print('\33[31;1mERRO! Favor digitar número inteiro válido.\33[m')
        else:
            break
    return n.title() + ';' + i


def verarq(f):
    try:
        a = open(f, 'rt')
    except:
        a = open(f, 'wt+')
    finally:
        a.close()


def adicionar(d, b):
    try:
        f = open(b, 'at')

        f.write(d + '\n')
        f.close()
    except:
        print('Algo deu errado!')


def title(t):
    print('=' * 35)
    print(f'{t.upper():^35}')
    print('=' * 35)
