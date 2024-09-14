from curses.ascii import isalpha
from utilidadescev import moeda

def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\n\033[0;31mERRO: \"{entrada}\" Preço inválido\033[m')
        else:
            valido = True
            return float(entrada)
