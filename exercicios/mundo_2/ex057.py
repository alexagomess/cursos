'''Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. 
Caso esteja errado, peça a digitação novamente até ter um valor correto.'''


sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('\nVocê digitou o sexo errado. Digite seu sexo [M/F]: ')).strip().upper()[0]
print('\nVocê digitou corretamente! Fim do programa.')
