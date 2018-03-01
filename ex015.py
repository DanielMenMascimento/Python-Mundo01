'''Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e
a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o
carro custa R$60 por dia e R$0,15 por Km rodado.'''

print('=' * 90)
dia = int(input('Quantos dias de aluguel? '))
km = float(input('Quantos km rodados? '))

pagar = (dia * 60) + (km * 0.15)

print('Depois de rodar {:.2f}km em {} dias, você deve pagar R${:.2f} para a locadora do veículo.'.format(km, dia, pagar))
