# import math
# num = int(input('Digite um numero: '))
# raiz = math.sqrt(num)
# print('A raiz quadrada de {} é de {:.2f}'.format(num, raiz))
# # print('A raiz quadrada de {} é de {}'.format(num, math.ceil(raiz))) #O ceil arredonda pra cima
# # print('A raiz quadrada de {} é de {}'.format(num, math.floor(raiz))) #O ceil arredonda pra baixo


# from math import sqrt
# num = int(input('Digite um numero: '))
# raiz = sqrt(num)
# print('A raiz quadrada de {} é de {:.2f}'.format(num, raiz))
# # print('A raiz quadrada de {} é de {}'.format(num, ceil(raiz))) #O ceil arredonda pra cima
# # print('A raiz quadrada de {} é de {}'.format(num, floor(raiz))) #O ceil arredonda pra baixo


# import cpf
# qtd = int(input('Quantos CPF vc quer gerar? '))
# print(cpf.gerar(qtd))

# import cpf
# numcpf = str(input('Qual CPF vc quer validar? '))
# validacpf = cpf.checar(numcpf)
# print('A validação do CPF {} foi {}'.format(numcpf, validacpf))

# import emoji
# print(emoji.emojize('Olá mundo! :smiling_face_with_sunglasses:'))


import zipfile
with zipfile.ZipFile("sinqia_custodia_14653_file.zip", "r") as myzip:
    myzip.extractall("extracted_files")

# import mimetypes
# mime_type, encoding = mimetypes.guess_type("sinqia_custodia_14653_file.zip")
# print(f"MIME type: {mime_type}, Encoding: {encoding}")