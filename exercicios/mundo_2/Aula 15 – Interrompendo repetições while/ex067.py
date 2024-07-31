"""Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo."""

while True:
    num = int(input("\nQuer ver a tabuada de qual valor? "))
    if num < 0:
        break
    print('-'*30)
    for cont in range(1,11):
        result = num * cont
        print(f'{num} x {cont} = {result}')
    print('-'*30)
print('\nAcabou o programa!')
