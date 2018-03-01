# Sen Cos e Tan

from math import radians, sin, cos, tan

angulo = float(input('Digite um ângulo: '))
seno = sin(radians(angulo))
cosseno = cos(radians((angulo)))
tangente = (tan(radians(angulo)))

print('O ângulo de {}° tem:\n SEN = {:.2f}\n COS = {:.2f}\n TAN = {:.2f}'.format(angulo, seno, cosseno, tangente))
