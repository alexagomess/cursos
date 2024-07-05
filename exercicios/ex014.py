#Escreva um programa que converta uma temperatura digitada em C e converta para F

temp = float(input('Digite uma temperatura em C: '))

f = ((9 * temp) / 5) + 32

print('A temperatura {} em C quando convertida para F fica em {}'.format(temp, f))
