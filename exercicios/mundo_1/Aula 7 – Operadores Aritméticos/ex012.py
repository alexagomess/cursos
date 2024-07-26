#Faça um algoritmo que leia um preço de um produto e mostre seu novo preço, com 5% de desconto

produto = float(input('Digite o preço de um produto: R$'))

desconto = produto * 0.05
novopreco = produto - desconto

print('O desconto de 5% foi de R${:.2f}, sendo assim o novo preço do produto é de R${:.2f}'.format(desconto, novopreco))
