"""Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável."""

def escreva(frase):
    tam = len(frase) + 4
    print('~' * tam)
    print(f'  {frase:^}')
    print('~' * tam)


escreva('Gustavo Guanabara')
escreva('Curso de Python no YouTube')
escreva('CeV')
