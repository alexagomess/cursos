# Faça um programa que leia uma frase pelo teclado e mostre:
## Quantas vezes aparece a letra "A"
## Em que posição ela aparece a primeira vez
## Em que posição ela aparece a última vez

frase = str(input('Digite uma frase: ')).strip().upper()

qtd = frase.upper().count('A')
primeiraposicao = frase.find('A')+1 #--Poderia usar o upper no método
ultimaposicao = frase.rfind('A')+1 #--Poderia usar o upper no método

print(frase)
print('A letra "A" apareceu {} vezes.'.format(qtd))
print('A primeira posição da letra "A" é: {}'.format(primeiraposicao))
print('A ultima posicao da letra "A" é: {}'.format(ultimaposicao))
