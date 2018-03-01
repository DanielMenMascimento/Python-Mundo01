# Criar um algorítimo que pede 4 notas e exibe média das notas de um aluno

n1 = float(input('NOTA 1: '))
n2 = float(input('NOTA 2: '))
n3 = float(input('NOTA 3: '))
n4 = float(input('NOTA 4: '))

m = (n1 + n2 + n3 + n4) / 4

print('A média é {:.2f}'.format(m))
