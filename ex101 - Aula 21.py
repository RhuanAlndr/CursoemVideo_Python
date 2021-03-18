def voto(ano):
    from datetime import date
    global i
    i = date.today().year - ano
    if i < 16:
        return 'VOTO NEGADO!'
    elif i < 18 or i >= 65:
        return 'VOTO OPCIONAL!'
    else:
        return 'VOTO OBRIGATÓRIO!'


i = int(input('Em que ano você nasceu? '))
print(f'A pessoa tem {i}. {voto(i)}')
