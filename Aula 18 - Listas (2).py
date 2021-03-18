'''test = list()
test.append('Gustavo')
test.append(40)
guys = list()
guys.append(test[:])
test[0] = 'Maria'
test[1] = 22
guys.append(test[:])
print(guys)'''

'''guys = list()
data = list()
mai = men = 0
for c in range(0, 5):
    data.append(input('Nome: '))
    data.append(int(input('Idade: ')))
    guys.append(data[:])
    data.clear()

for p in guys:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        mai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        men += 1
print(f'Temos {men} menores de idade e {mai} maiores de idade.')'''
