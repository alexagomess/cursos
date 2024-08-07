'''Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.'''


listagem = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')

for palavra in listagem:
    print(f'\nPara a palavra {palavra.upper()}, nós temos as vogais: ', end=' ')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(f'{letra.upper()}', end=' ')
