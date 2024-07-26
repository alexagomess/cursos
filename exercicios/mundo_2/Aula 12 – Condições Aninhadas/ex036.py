#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa,
## o salário do comprador e em quantos anos ele vai pagar.
### Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

valor_casa = float(input('Qual o valor da casa que vc quer comprar? R$'))
salario = float(input('Qual seu salário bruto por mês? R$'))
anos_emprestimo = int(input('Em quantos anos vc quer pagar o empréstimo? '))
meses_emprestimo = anos_emprestimo * 12

prestacao_mensal = valor_casa / meses_emprestimo

print(f'\nSegundo os dados informados, a prestação mensal será no valor de R${prestacao_mensal:.2f} durante {anos_emprestimo} anos.\n')

percentual_salario = prestacao_mensal / salario * 100

if percentual_salario > 33:
    print(f'Por isso seu empréstimo foi NEGADO! O valor da prestação comprometeu {percentual_salario:.1f}% do seu salário bruto mensal, acima do limite de 33%.')
else:
    print(f'Por isso seu empréstimo foi APROVADO! O valor da prestação comprometeu {percentual_salario:.1f}% do seu salário bruto mensal, abaixo do limite de 33%.')
