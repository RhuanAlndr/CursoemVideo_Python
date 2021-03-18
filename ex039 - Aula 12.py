from datetime import date
an = (int(input('Em que ano você nasceu? ')))
s = (int(input('Se você for homem digite 1 e 2 se for mulher'
               '\ndigite sua escolha: ')))
i = date.today().year - an
if s == 1:
    if i < 18 and not i == 17:
        print('Ainda falta {:.0f} anos para você se apresentar.'.format(18 - i))
    elif i == 17:
        print('Ainda falta {:.0f} ano para você se apresentar.'.format(18 - i))
    elif i == 18:
        print('Está na hora de você se alistar!')
    elif i == 19:
        print('Você provavelmente se alistou há {:.0f} ano'.format(i - 18))
    else:
        print('Você provavelmente se alistou há {:.0f} anos'.format(i - 18))
elif s == 2:
    print('Você tem {:.0f} e não precisa se alistar.'.format(i))
else:
    print('Favor digitar um 1 ou 2 para sexo.')
