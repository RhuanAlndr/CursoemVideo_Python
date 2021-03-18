c = float(input('Qual o valor da casa? R$'))
s = float(input('Quanto é o seu salário? R$'))
t = int(input('Em quantos anos você quer pagar a casa? '))
vp = c / (t * 12)
vm = s / 100 * 30
if vp <= vm:
    print('O valor da sua prestação é R${:.2f}'.format(vp))
else:
    print('\33[1;31mDesculpe não podemos realizar o empréstimo!\33[m')
    print('O valor máximo de prestação que podemos aprovar para você é'
          '\nR${:.2f} e nesse caso a prestação seria R${:.2f}'.format(vm, vp))
