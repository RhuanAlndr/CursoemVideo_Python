def notas(*n, sit=False):
    """
    Função para analizar notas e situação de vários alunos
    :param n: uma ou mais notas de alunos
    :param sit: (opcional) mostra a situação do aluno
    :return: retorna o dicionário com notas e situação do aluno
    """
    d = dict()
    d['total'] = len(n)
    d['maior'] = max(n)
    d['menor'] = min(n)
    d['média'] = sum(n)/len(n)
    if sit:
        if d['média'] <= 6:
            d['situação'] = 'Ruim'
        elif d['média'] < 8:
            d['situação'] = 'Razoavel'
        else:
            d['situação'] = 'Boa'
    return d


r = notas(10, 10, 5, 10, sit=True)
print(r)
