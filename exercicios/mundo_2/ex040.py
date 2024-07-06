"""Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
- Média abaixo de 5.0: REPROVADO
-  Média entre 5.0 e 6.9: RECUPERAÇÃO
-  Média 7.0 ou superior: APROVADO
"""

nota_1 = float(input('Digite a primeira nota: '))
nota_2 = float(input('Digite a segunda nota: '))

media = (nota_1 + nota_2) / 2

if media < 5.0:
    print(f'\nVocê está REPROVADO! Sua média foi de {media}.')
elif media >= 5.0 and media <= 6.9:
    print(f'\nVocê está em RECUPERAÇÃO! Sua média foi de {media}.')
else:
    print(f'\nVocê está APROVADO! Sua média foi de {media}.')
