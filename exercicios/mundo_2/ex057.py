'''Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. 
Caso esteja errado, peça a digitação novamente até ter um valor correto.'''


sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()
while sexo != 'M' and sexo != 'F':
    print('\nVocê digitou o sexo errado. Digite novamente!')
    sexo = str(input('\nDigite seu sexo [M/F]: ')).strip().upper()
print('\Você digitou corretamente! Fim do programa.')
