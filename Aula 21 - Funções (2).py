'''print(input.__doc__)'''



'''funções com parametros variaveis'''
def somar(a=0, b=0, c=0):
    s = a + b + c
    print(f'A soma dos números deu {s}')

somar()



'''escopo de variaveis'''
def função():
    n1 = 2
    print(f'N1 dentro vale {n1}')

n1 = 4
função()
print(f'N1 fora vale {n1}')

help(print)
