"""A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e
    mostre sua caategoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JUNIOR
- Até 25 anos: SENIOR
- Acima: MASTER"""

from datetime import date

ano_nascimento = int(input('Digite o ano do seu nascimento (YYYY): '))

data_atual = date.today().year
diferenca_anos = data_atual - ano_nascimento

if diferenca_anos <= 9:
    print(f'\nVocê tem {diferenca_anos} anos. Sua categoria é MIRIM.')
elif diferenca_anos <= 14:
    print(f'\nVocê tem {diferenca_anos} anos. Sua categoria é INFANTIL.')
elif diferenca_anos <= 19:
    print(f'\nVocê tem {diferenca_anos} anos. Sua categoria é JUNIOR.')
elif diferenca_anos <= 25:
    print(f'\nVocê tem {diferenca_anos} anos. Sua categoria é SENIOR.')
else:
    print(f'\nVocê tem {diferenca_anos} anos. Sua categoria é MASTER.')
