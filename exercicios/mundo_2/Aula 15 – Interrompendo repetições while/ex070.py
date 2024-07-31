"""Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) Qual é o total gasto na compra.
B) Quantos produtos custam mais de R$1000.
C) Qual é o nome do produto mais barato."""

print("=-"*15)
print("MERCADO DA PAZ")
print("=-"*15)

cont = total_compra = qtd_produtos_mais_mil_reais = preco_produto_mais_barato = 0
nome_produto_mais_barato = ' '

while True:
    nome = str(input('\nDigite o nome de um produto: '))
    preco = float(input('Digite o preço do produto: R$'))

    total_compra += preco
    cont += 1

    if preco >= 1000:
        qtd_produtos_mais_mil_reais += 1

    if cont == 1 or preco < preco_produto_mais_barato:
        nome_produto_mais_barato = nome
        preco_produto_mais_barato = preco

    resposta = ' '
    while resposta not in 'SsNn':
        resposta = str(input('\nQuer continuar? [S/N] ')).strip().upper()[0]
    if resposta == 'N':
        break

print(f'\nO total gasto na compra foi de R${total_compra:.2f}.')
print(f'{qtd_produtos_mais_mil_reais} produtos custaram mais de R$ 1000.00.')
print(f'O nome do produto mais barato foi: {nome_produto_mais_barato} que custou R${preco_produto_mais_barato:.2f}.')
