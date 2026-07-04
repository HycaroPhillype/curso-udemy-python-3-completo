import re
import sys
# cpf = input('Digite seu CPF (apenas números): ') \
#     .replace('.', '') \
#     .replace('-', '')\
#     .replace(' ', '')

cpf = input('Digite seu CPF (apenas números): ') 
cpf_valid = re.sub(r'[^0-9]', '', cpf)  # Remove qualquer caractere que não seja número
# cpf_list = cpf.replace('.', '')

cpf_repetido = cpf_valid == cpf_valid[0] * len(cpf_valid)
if cpf_repetido:
    print('CPF com números repetidos, inválido')
    sys.exit()
soma = 0
for i in range(9):
    soma += int(cpf_valid[i]) * (10 - i)
digito = (soma * 10) % 11
digito = digito if digito <= 9 else 0
print(f'O primeiro dígito do CPF {cpf_valid} é {digito}')
if cpf_valid[9] == str(digito):
    print('CPF válido')  
else:
    print('CPF inválido')

cpf_segundo_gito = cpf_valid[:9] + str(digito)

soma = 0

for i in range(10):
    soma += int(cpf_segundo_gito[i]) * (11 - i)
digito2 = (soma * 10) % 11
digito2 = digito2 if digito2 <= 9 else 0
print(f'O segundo dígito do CPF {cpf_segundo_gito} é {digito2}')
if cpf_valid[9] == str(digito) and cpf_valid[10] == str(digito2):
    print('CPF válido')
else:
    print('CPF inválido')