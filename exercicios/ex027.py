# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
## Ex: Ana Maria de Souza
### primeiro = Ana
### último = Souza

nome = str(input('Digite o nome completo de uma pessoa: ')).strip()

dividido = nome.split()

print('O nome digitado foi: {}'.format(nome.title()))
print('O primeiro nome da pessoa é: {}.'.format(dividido[0].title()))
print('O ultimo nome da pessoa é: {}'.format(dividido[len(dividido)-1].title()))
