#Crie um programa que leia o nome completo de uma pessoa e mostre:
## O nome com todas as letras maiusculas
## O nome com todas as letras minusculas
## Quantas letras ao todo (sem considerar os espaços)
## Quantas letras tem o primeiro nome

nome = input('Digite seu nome completo: ').strip()
maiusculas = nome.upper()
minusculas = nome.lower()
join  = ''.join(nome.split())
quantidade = len(join)
split = nome.split()

print('Seu nome é: {}'.format(nome))
print('Em letras maíusculas: {}'.format(maiusculas))
print('Em letras minusculas: {}'.format(minusculas))
print('Seu nome sem espaços é {}.'.format(join))
# print('A quantidade de letras sem espaços é {}.'.format(quantidade)) #--tem essa forma de fazer, splita toda a string e concatena por nada
print('A quantidade de letras sem espaços é {}.'.format(len(nome) - nome.count(" "))) #-- tbm tem essa forma, contar quantos espaços tem e subtrair ele do saldo final
print('Primeiro nome: {}'.format(split[0]))
print('Seu primeiro nome tem {} letras.'.format(len(split[0])))
