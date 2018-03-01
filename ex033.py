# maior e menor valor

a = int(input('1º valor: '))
b = int(input('2º valor: '))
c = int(input('3° valor: '))
# Verificando o menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
#Verificando o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
# Mostrando o resultado
print('O menor valor foi {}'.format(menor))
print('O maior valor foi {}'.format(maior))
