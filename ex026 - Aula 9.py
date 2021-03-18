f = input('Escreva uma frase qualquer: ').strip().lower()
print('A letra "a" aparece {} na sua frase.'.format(f.count('a')))
print('A letra "a" aparece a primeira vez na posição {}.'.format(f.find('a') + 1))
print('A letra "a" aparece pela última vez na posição {}.'.format(f.rfind('a') + 1))
