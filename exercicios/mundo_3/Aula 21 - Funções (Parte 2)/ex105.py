'''Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e 
vai retornar um dicionário com as seguintes informações:
- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)
Adicione também as docstrings da função.'''


def notas(*valores, situacao=False):
    """
    Função para analisar notas e situações de vários alunos.
    :param valores: uma ou mais notas dos alunos (aceita várias).
    :param situacao: valor opcional, indicando se seve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situação da turma.
    """
    dicionario = dict()
    dicionario['total'] = len(valores)
    dicionario['maior'] = max(valores)
    dicionario['menor'] = min(valores)
    dicionario['média'] = sum(valores) / len(valores)

    if situacao:
        if dicionario['média'] >= 7:
            dicionario['situação'] = 'BOA'
        elif dicionario['média'] >= 5:
            dicionario['situação'] = 'RAZOÁVEL'
        else:
            dicionario['situação'] = 'RUIM'
    return dicionario


resp = notas(5.5, 2.5, 1.5)
print(resp)
