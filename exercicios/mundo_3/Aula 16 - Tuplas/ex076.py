'''Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
No final, mostre uma listagem de preços, organizando os dados em forma tabular.'''

print("=-"*15)
print(f'{"MERCADO DA PAZ":^30}')
print("=-"*15)

listagem = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)

metade_listagem = int(len(listagem) / 2)

for cont in range(0, metade_listagem):
    produto = listagem[0::2]
    preco = listagem[1::2]
    print(f'{produto[cont]:.<20}', end=' ')
    print(f'R$ {preco[cont]:>6.2f}')
