import random  
import sys


for _ in range(10):
    cpf = ''
    for i in range(9):
        cpf += str(random.randint(0, 9))

    soma = 0 

    for i in range(9):
        soma += int(cpf[i]) * (10 - i)
    digito = (soma * 10) % 11
    digito = digito if digito <= 9 else 0

    cpf_segundo_gito = cpf[:9] + str(digito)

    soma = 0

    for i in range(10):
        soma += int(cpf_segundo_gito[i]) * (11 - i)
    digito2 = (soma * 10) % 11
    digito2 = digito2 if digito2 <= 9 else 0

    cpf_gerado = f'{cpf}{digito}{digito2}'
    print(cpf_gerado)