n1 = int(input('Digite um número: '))
n2 = int(input('Agora outro número: '))
n3 = int(input('Por favor um último número: '))
# Analisando o maior número
if n1 > n2 and n1 > n3:
    maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
# Analisando o menor número
if n1 < n2 and n1 < n3:
    menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
# mostrando os resultados
print('O menor número é {}'.format(menor))
print('O maior número é {}'.format(maior))
