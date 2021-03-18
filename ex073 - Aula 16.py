tb = 'Atlético-MG', 'Vasco da Gama', 'Internacional', 'Bahia', 'Athetico-PR', 'Grêmio', 'Atlético-GO', 'Santos',\
     'Fluminense', 'Sport Recife', 'São Paulo', 'Flamengo', 'Palmeiras', 'Botafogo', 'Bragantino-SP', 'Corinthans',\
     'Goiás', 'Ceará SC', 'Fortaleza', 'Coritiba'
print(f'Os cinco primeiros são {tb[0:5]}')
print(f'Os quatro últimos são {tb[-4:]}')
print(f'Times em ordem alfabética {sorted(tb)}')
print(f'O São Paulo está na {tb.index("São Paulo") + 1}ª posição.')
