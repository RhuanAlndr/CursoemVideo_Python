def ficha(nome, gols):
    if len(nome) == 0:
        nome = '<Desconhecido>'
    if len(gols) == 0 or gols.isalpha():
        gols = 0
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato')


nome = input('Nome do jogador: ')
gols = input('Número de gols: ')
ficha(nome, gols)
