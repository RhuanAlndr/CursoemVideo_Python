a = dict()
a['nome'] = str(input('Nome do aluno: '))
a['média'] = float(input(f'Média de {a["nome"]}: '))
if a['média'] >= 7:
    a['situação'] = 'Aprovado'
elif 5 <= a['média'] < 7:
    a['situação'] = 'Recuperação'
else:
    a['situação'] = 'Reprovado'
for k, i in a.items():
    print(f'{k.title()} é igual a {i}')
