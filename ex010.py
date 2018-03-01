# Conversor de moeda

dolar = float(input('Quanto está custando o dólar atualmente? US$ '))
din = float(input('Quantos reais você tem? R$ '))

print('Com R${:.2f}, você pode comprar US${:.2f}'.format(din, din / dolar))
