# Conta quantas vezes uma letra aparece e em quais posições

letra = str(input('Que letra você busca? ')).lower()
frase = str(input('Digite uma frase: ')).strip()
print('A letra "{}" aparece {} vezes na frase'.format(letra, frase.lower().count(letra)))
print('A primeira ocorrência da letra "{}" foi na casa {}'.format(letra, frase.lower().find(letra)+1))
print('A última ocorrência da letra "{}" foi na casa {}'.format(letra, frase.lower().rfind('a')+1))
