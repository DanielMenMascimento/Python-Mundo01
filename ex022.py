# Formatando String, contando quantas letras tem (sem contar espaços) e contando quantas letras tem o primeiro nome

nome = str(input('Digite seu nome inteiro: ')).strip()

print('Seu nome em maiúsculo é: {}'.format(nome.upper()))
print('Seu nome em minúsculo é: {}'.format(nome.lower()))
print('Seu nome capitalizado é: {}'.format(nome.capitalize()))
print('Seu nome titulazado é: {}'.format(nome.title()))
print('=' * 50)
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
