p = float(input('Qual é o seu peso? '))
a = float(input('Qual sua altura? '))
imc = p / (a ** 2)
if imc < 18.5:
    print('Seu imc é {:.1f} e você está \33[33mabaixo do peso!\33[m'.format(imc))
elif 18.5 <= imc < 25:
    print('Seu imc é {:.1f} e você está com \33[34mpeso ideal!\33[m'.format(imc))
elif 25 <= imc < 30:
    print('Seu imc é {:.1f} e você está com \33[35msobre peso!\33[m'.format(imc))
elif 30 <= imc < 40:
    print('Seu imc é {:.1f} e você está com \33[31mobesidade!\33[m'.format(imc))
else:
    print('Seu imc é {:.1f} e você está com \33[1;31mobesidade mórbida!\33[m'.format(imc))
