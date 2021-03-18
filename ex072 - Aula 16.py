ne = 'zero', 'um', 'dois', 'três', 'quatro',\
     'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',\
     'onze', 'doze', 'treze', 'quatorze', 'quinze',\
     'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
n = int(input('Digite um número entre 0 e 20: '))
while True:
    if 0 <= n <= 20:
        break
    n = int(input('Desculpe, digite novamente um número entre 0 e 20: '))
print(f'Você digitou o número {ne[n]}.')
