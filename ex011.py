# Criar um algorítimo para calcular quantos litros de tinta serão necessários para pintar uma parede leevando em conta 1l para cada 2m²

largura = float(input('Largura da parede: '))
altura = float(input('Altura da paede: '))
area = largura * altura
tinta = area / 2

print('Sua parede tem {:.2f} x {:.2f} com uma área de {:.2f}m².'.format(largura, altura, area))
print('Logo será necessário {:.1f}l de tinta para pintar a parede inteira.'.format(tinta))
