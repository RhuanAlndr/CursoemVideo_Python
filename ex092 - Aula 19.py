from datetime import date
c = dict()
c['nome'] = input('Nome: ')
a = int(input('Ano de nascimento: '))
c['idade'] = date.today().year - a
c['ctps'] = input('Carteira de Trabalho (0 não tem): ')
if c['ctps'] != 0:
    c['contratação'] = int(input('Ano de contatação: '))
    c['salário'] = float(input('Salário: R$ '))
    c['aposentadoria'] = c['contratação'] + 35 - a
print(c)
for c, v in c.items():
    print(f'{c.title()} tem o valor {v}')
