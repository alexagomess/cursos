"""Elabore um programa que calcule o valor a ser pago por um produto, considerando seu preço normal e condição de pagamento:
- A vista dinheiro/cheque: 10% de desconto
- A vista no cartão: 5% de desconto
- Em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros
"""

preco_produto = float(input('\nDigite o preço do produto: R$'))
print('\nEscolha a forma de pagamento:')
print('1 - A vista dinheiro')
print('2 - A vista cartão')
print('3 - 2x no cartão')
print('4 - 3x ou mais no cartão')
forma_pagamento = int(input('\nDigite sua opção: '))

if forma_pagamento == 1:
    percentual_desconto = 0.10
    valor_desconto = percentual_desconto * preco_produto
    preco_final = preco_produto - valor_desconto
    print(f'\nVocê teve um desconto de 10% no valor de R${valor_desconto:.2f}. O valor final do produto com desconto é de R${preco_final:.2f}.')
elif forma_pagamento == 2:
    percentual_desconto = 0.05
    valor_desconto = percentual_desconto * preco_produto
    preco_final = preco_produto - valor_desconto
    print(f'\nVocê teve um desconto de 5% no valor de R${valor_desconto:.2f}. O valor final do produto com desconto é de R${preco_final:.2f}.')
elif forma_pagamento == 3:
    print(f'\nVocê não teve desconto e pagará o valor normal do produto de R${preco_produto:.2f}.')
elif forma_pagamento == 4:
    percentual_juros = 0.20
    valor_juros = percentual_juros * preco_produto
    preco_final = preco_produto + valor_juros
    print(f'\nO produto teve 20% de juros no valor de R${valor_juros:.2f}. O valor final do produto com juros é de R${preco_final:.2f}.')
else:
    print('\nVocê não digitou uma opção válida! Programa encerrado.')
