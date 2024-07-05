# Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem, cobrando R$0,50 por km para viagens de até 200km e R$0,45 para viagens mais longas.

viagem = float(input('Qual a distância em km da viagem que vc quer fazer? '))

if viagem <= 200:
    valor_km = 0.50
    valor_passagem = viagem * valor_km
else:
    valor_km = 0.45
    valor_passagem = viagem * valor_km
print('O preço de sua passagem é de R${:.2f}. '.format(valor_passagem))
