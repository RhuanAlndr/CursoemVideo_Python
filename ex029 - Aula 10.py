v = int(input('Em quantos Km/h você estava? ').strip())
if v > 80:
    print('Você ultrapassou o limite de velocidade!\nVocê estava a {}Km/h e sua multa é R${:.2f}'.format(v, (v - 80) * 7))
else:
    print('Muito bem continue a dirigir com segurança!')
