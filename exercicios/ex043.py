"""Desenvolva uma lógica que leia o peso e altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
- Abaixo de 18.5: Abaixo do peso
- Entre 18.5 e 25: Peso ideal
- 25 até 30: Sobrepeso
- Acima de 40: Obesidade mórbida
"""

peso = float(input('Digite seu peso em kg (ex.: 69.2): '))
altura = float(input('Digite sua altura em metros (ex.: 1.70): '))

imc = peso / (altura ** 2)

if imc < 18.5:
    print(f'\nVocê está abaixo do peso. Seu IMC é de {imc:.1f}.')
elif imc >= 18.5 and imc <= 25:
    print(f'\nVocê está no peso ideal. Seu IMC é de {imc:.1f}.')
elif imc > 25 and imc <= 30:
    print(f'\nVocê está em sobrepeso. Seu IMC é de {imc:.1f}.')
else:
    print(f'\nVocê está com obesidade morbida. Seu IMc é de {imc:.1f}.')
