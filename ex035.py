# Condicional composta (Criando um triângulo)

r1 = float(input('1º segmento: '))
r2 = float(input('2º segmento: '))
r3 = float(input('3º segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PEDEM formar um triângulo!')
else:
    print('Os segmentos acima NÃO PODEM formar um triângulo!')
