# Criar um algorítimo que tira a porcentagem de um valor

desc = int(input('De quantos % será o desconto? %'))
v = float(input('Quanto custa o produto? R$'))
# total = (v * desc) / 100

print('O produto que custa R${:.2f}, com o desconto de {}% custará R${:.2f}.'.format(v, desc, v - (v * desc / 100)))
