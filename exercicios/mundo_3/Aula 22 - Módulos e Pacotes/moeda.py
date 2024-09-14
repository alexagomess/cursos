def aumentar(num = 0, taxa = 0, format=False):
    """
    :param num: número informado pelo usuário
    :param taxa: valor número para calcular a taxa
    :param format: formatar o número como R$
    """
    total = (num * taxa/100) + num
    return total if format==False else moeda(total)

def diminuir(num = 0, taxa = 0, format=False):
    total = num - (num * taxa/100)
    return total if format==False else moeda(total)

def dobro(num = 0, format=False):
    total = num * 2
    return total if format == False else moeda(total)

def metade(num = 0, format=False):
    total = num / 2
    return total if format == False else moeda(total)

def moeda(num = 0, moeda = 'R$'):
    return f'{moeda}{num:>.2f}'.replace('.', ',')
    
def resumo(num = 0, taxa_mais = 0, taxa_menos = 0):
    print('-'*35)
    print('Resumo do valor'.center(35))
    print('-'*35)
    print(f'Preço analisado: \t{moeda(num)}')
    print(f'Dobro do preço: \t{dobro(num, True)}')
    print(f'Metade do preço: \t{metade(num, True)}')
    print(f'{taxa_mais}% de aumento: \t{aumentar(num, taxa_mais, True)}')
    print(f'{taxa_menos}% de redução: \t{diminuir(num, taxa_menos, True)}')
    print('-'*35)
    return