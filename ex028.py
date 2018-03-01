# Jogo da adivinhação

 from random import randint
  
 n = randint(0, 5)
user = int(input('Pensei em um número entre 0 e 5. Qual você acha q foi? '))

print('Eu penseo no número {} e você desse que foi o {}, pelo visto você é ...'.format(n, user))

if user == n:
    print('Sortudo(a), porque poucos conseguem acertar :(')
else:
    print('Só mais um(a), ja era de se esper :D')
    
