#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. Considere 1 dólar a R$ 3,27

carteira = float(input('Quantos reais você tem na carteira? R$'))

dolar = carteira / 3.27

print('Com R${:.2f} você consegue comprar US${:.2f}.'.format(carteira, dolar))
