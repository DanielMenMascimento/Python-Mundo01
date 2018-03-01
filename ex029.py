# Calcula a multa do carro com base em R$7,00 para cada 1km acima do permitido

velocidade = float(input('Qual é a velocidade atual do carro? '))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('MULTADO! Você excedeu o limite permitido que é de 80km/h')
    print('Com o valor de R$7,00 por km excedido, você deve pagar pagar R${:.2f} por passar a {:.0f}km/h'.format(multa, velocidade))
print('Tenha um bom dia! Dirija co msegurança!')
