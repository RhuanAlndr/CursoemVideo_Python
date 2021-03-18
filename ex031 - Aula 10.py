km = int(input('Quantos Km serão a sua viagem? '))
if km > 200:
    print('Sua viagem custará R${:.2f}'.format(km * 0.45))
else:
    print('Sua viagem custará R${:.2f}'.format(km * 0.50))
