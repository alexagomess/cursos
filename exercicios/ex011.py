#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m2.

largura = float(input('Digite a largura da parede: '))
altura = float(input('Agora digite a altura: '))

metrosquadrados = largura * altura
tinta = metrosquadrados / 2

print('Baseado na largura de {:.2f} e altura de {:.2f}, sua parede tem {:.2f} metros quadrados. Sendo assim, vc precisa de {:.1f} litro(s) de tinta.'.format(largura, altura, metrosquadrados, tinta))
