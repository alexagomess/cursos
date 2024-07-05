# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome

nome = str(input('Digite o nome de uma pessoa: ')).strip()

## Tem esse primeiro jeito de fazer, uso o find pra encontrar o SILVA. Se não tiver sempre vai ser -1, então faço um validador se o resultado encontrado é diferente de -1
# validador = nome.upper().find('SILVA')
# print(validador != -1)

## Aqui eu só valido se Silva está dentro de nome. Se sim, é true
validador = 'SILVA' in nome.upper()
print(validador)
