'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
- A média de idade do grupo.
- Qual é o nome do homem mais velho.
- Quantas mulheres têm menos de 20 anos.
'''

count_mulheres_menor_20 = 0
nome = 0
maior_idade = 0
soma_idade = 0

for c in range(1, 5):
    nome = str(input('Digite o nome da pessoa: ')).strip().lower()
    idade = int(input('Digite a idade da pessoa: '))
    sexo = str(input('Digite o sexo da pessoa [M/F]: ')).strip().lower()
    print('\n')

    soma_idade = soma_idade + idade
    
    if sexo == 'm':
        if c == 1:
            maior_idade = idade
            nome_homem_mais_velho = nome
        else:
            if idade > maior_idade:
                maior_idade = idade
                nome_homem_mais_velho = nome

    if sexo == 'f' and idade < 20:
        count_mulheres_menor_20 = count_mulheres_menor_20 + 1

media_idade = soma_idade / c

print(f'\nA média de idade do grupo é {media_idade:.0f} anos.')
print(f'\nO homem mais velho é {nome_homem_mais_velho.title()}.')
print(f'\nO total de mulheres com menos de 20 anos é {count_mulheres_menor_20}.')
print('\n')
