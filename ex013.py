#  Criar um algorítimo que calcula o reajuste salarial

sa = float(input('Quanto o funcionário recebe atualmente? R$'))
a = float(input('De quantos % será o reajuste? %'))

print('O funcionário que recebe R${:.2f}, com um reajuste de {:.0f}% receberá R${:.2f}.'.format(sa, a, sa + (sa * a / 100)))
