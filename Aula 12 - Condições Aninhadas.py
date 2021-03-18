n = str(input('Qual é o seu nome? ')).lower()
if n == 'gustavo':
    print('Que nome bonito!')
elif n == ('joao' or 'maria' or 'pedro' or 'paulo'):
    print('Seu nome é bem popular no Brasil.')
elif n in ('juliana ana'):
    print('Você tem um belo nome feminino!')
else:
    print('Que nome normal.')
print('Tenha um bom dia, {}!'.format(n.title()))
