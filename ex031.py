# Porcentagem com condicional

distancia = float(input('Qual é a distância da sua viagem? '))

# preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45

if distancia <= 200:
    print('você está prestes a começar uma viagem de {:.0f}km!'.format(distancia))
    preco = distancia * 0.50
else:
    print('Sente-se confortavelmente, pois sua longa viagem de {:.0f}km começa agora!'.format(distancia))
    preco = distancia * 0.45

print('Sua viagem custará R${:.2f}'.format(preco))
