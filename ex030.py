# par ou impar

n = int(input('Digite um número: '))
result = n % 2

if result == 0:
    print('O número {} é PAR!'.format(n))
else:
    print('O número {} é IMPAR!'.format(n))
