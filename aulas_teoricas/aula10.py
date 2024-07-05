# nome = str(input('Qual é o seu nome? ')).strip().upper()
# if nome == 'ADRIELLY':
#     print('É minha bonitinha!')
# else:
#     print('É fake natty!!')
# print('\nFim da validação!')


n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
print('\nA sua média foi {:.2f}.\n'.format(media))

if media >= 6.0:
    print('Sua média foi boa, parabéns!')
else:
    print('Sua média foi ruim, estude mais.')
