# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada km acima do limite.

velocidade = float(input('Digite a velocidade do carro em km/h: '))

if velocidade > 80:
    multa = 7
    diferenca = velocidade - 80
    valor_multa = diferenca * multa
    print('O carro estava acima do limite de velocidade! A multa foi no valor de R${:.2f}'.format(valor_multa))
else:
    print('O carro estava abaixo do limite.')
