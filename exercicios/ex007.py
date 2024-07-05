#Desenvolva um programa que leia as duas notas de um auno, calcule e mostre a sua média

nota1 = float(input('Digite a primeira nota do aluno: '))
nota2 = float(input('Digite a segunda nota do aluno: '))

media = (nota1 + nota2) / 2

print('As notas digitadas foram {:.1f} e {:.1f}, sendo que a média ficou em {:.1f}'.format(nota1, nota2, media))
