# Crie um algorítimo que disseca o valor atribuído à variável

v = input('Digite qualquer coisa: ') # Atribuindo o valor à variável
print('É do tipo', type(v))
print('É alfabético:', v.isalpha())
print('É numérico:', v.isalnum())
print('É alfanumérico:', v.isalphanum()) 
print('É formado apenas de ESPAÇOS:', v.isspace())
print('É maiúscolo:', v.isupper()) 
print('É nimúscolo:', v.islower())
print('É decimal:', v.isdecimal())
