# Criar um algorítimo que converte grandezas

medida = float(input('Uma distância em metros: '))
cm = medida * 100
mm = medida * 1000

print('{}m correspondem a {:.0f}cm e {:.0f}mm.'.format(medida, cm, mm))
