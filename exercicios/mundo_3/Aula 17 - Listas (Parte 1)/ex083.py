'''Crie um programa onde o usuário possa digitar uma expressão qualquer que use parênteses.
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.'''


frase = str(input('Digite uma expressão qualquer: ')).strip()
frase_com_espacos = ' '.join(frase)
frase_split = frase_com_espacos.split()

cont_abre = cont_fecha = 0

for letra in frase_split:
    if letra == '(':
        cont_abre += 1
    if letra == ')':
        cont_fecha += 1
    
if cont_abre == cont_fecha:
    print('\nA expressão está válida!')
else:
    print('\nA expressão está errada!')
