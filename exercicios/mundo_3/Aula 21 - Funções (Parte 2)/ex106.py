'''Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer.
Quando o usuário digitar a palavra 'FIM', o programa se encerrará. Importante: use cores.'''


def interactive_help(com):
    titulo(f'Acessando o manual do comando {com}')
    help(com)

def titulo(msg, cor = 0):
    tam = len(msg)

comando = ''
while True:
    titulo('Sistema de ajuda PyHelp')
    comando = str(input('\nDigite uma função para usar o interactive help: '))
    if comando.upper() == 'FIM':
        break
    else:        
        interactive_help(comando)
