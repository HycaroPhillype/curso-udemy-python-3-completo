cpf = input('Digite seu CPF (apenas números): ')
soma = 0
cpf_list = cpf.replace('.', '')
print(cpf_list)
for i in range(9):
    soma += int(cpf_list[i]) * (10 - i)
digito = (soma * 10) % 11
digito = digito if digito <= 9 else 0
print(f'O primeiro dígito do CPF {cpf_list} é {digito}')
if cpf_list[9] == str(digito):
    print('CPF válido')  
else:
    print('CPF inválido')

soma = 0
cpf_segundo_gito = cpf_list[:9] + str(digito)

for i in range(10):
    soma += int(cpf_segundo_gito[i]) * (11 - i)
digito2 = (soma * 10) % 11
digito2 = digito2 if digito2 <= 9 else 0
print(f'O segundo dígito do CPF {cpf_segundo_gito} é {digito2}')
if cpf_list[10] == str(digito2) and cpf_list[9] == str(digito):
    print('CPF válido')
else:
    print('CPF inválido')