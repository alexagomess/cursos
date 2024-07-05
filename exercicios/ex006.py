#Crie um algoritimo que leia um número e mostre o seu dobro, triplo e raiz quadrada

numero = int(input('Digite um número para calcular: '))

dobro = numero * 2
triplo = numero * 3
raiz = numero ** (1/2)

print('O número digitado foi {}, sendo: \n o dobro: {} \n o triplo: {} \n a raiz quadrada: {:.2f}'.format(numero, dobro, triplo, raiz))
