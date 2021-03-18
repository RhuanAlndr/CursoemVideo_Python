s = float(input('Qual é o seu salário? '))
if s <= 1250:
    n = (s / 100 * 15) + s
else:
    n = (s / 100 * 10) + s
print('O valor do seu salário com aumento é R${:.2f}'.format(n))
