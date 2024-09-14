'''Crie um pacote chamado unitilidadesCeV que tenha dois módulos internos chamados moeda e dado.
Transfira todas as funções utilizadas nos desafios 107 ao 109 para o primeiro pacote e mantenha tudo funcionando.'''

from utilidadescev import moeda

num = float(input('Digite um preço: R$ '))
moeda.resumo(num, 10, 19)
