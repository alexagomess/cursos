'''Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado. 
Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como uma função input(), mas com uma validação de dados para aceitar apenas valores que sejam monetários.'''

from utilidadescev import moeda, dado

num = dado.leiaDinheiro('Digite o preço: R$ ')
moeda.resumo(num, 10, 19)
