'''Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, 
retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.'''


def voto(ano_nascimento):
    from datetime import date
    from time import sleep

    ano_atual = date.today().year
    idade = ano_atual - ano_nascimento
    print('Analisando idade...')
    sleep(2)
    if idade < 16:
        return f'Você tem {idade} anos e seu voto é: NEGADO'
    elif 16 <= idade < 18 or idade > 65:
        return f'Você tem {idade} anos e seu voto é: OPCIONAL'
    else:
        return f'Você tem {idade} anos e seu voto é: OBRIGATÓRIO'

valor = int(input('Ano nascimento: '))
print(voto(valor))
