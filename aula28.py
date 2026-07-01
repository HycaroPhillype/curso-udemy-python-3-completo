from time import sleep

"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

usuario = ''

while not usuario.isdigit():
    usuario = input('Digite um número inteiro: ')
    if not usuario.isdigit():
        print('Isso não é um número inteiro. Tente novamente.')


numero = int(usuario)
if numero % 2 == 0:
    print(f'O número {numero} é par.')
else:
    print(f'O número {numero} é ímpar.')


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""


while True:
    nome = input('Digite seu nome: ')
    usuario = input('Digite a hora atual (0-23): ')

    if not usuario.isdigit():
        print('Isso não é um número inteiro. Tente novamente.')
        continue

    hora = int(usuario)
    if 0 <= hora <= 23:
        break
    print('Hora inválida. Tente novamente.')
          
if 0 <= hora <= 11:
    sleep(1)
    print(f'Bom dia, {nome}!')
    sleep(1)
elif 12 <= hora <= 17:
    sleep(1)
    print(f'Boa tarde, {nome}!')
    sleep(1)
else:
    sleep(1)
    print(f'Boa noite, {nome}!')
    sleep(1)


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

usuario = input('Digite seu primeiro nome: ')

tamanho_nome = len(usuario)

if tamanho_nome <= 4:
    print(f'Seu nome tem {tamanho_nome} letras, é curto.')
elif 5 <= tamanho_nome <= 6:
    print(f'Seu nome tem {tamanho_nome} letras, é normal.')
else:
    print(f'Seu nome tem {tamanho_nome} letras, é muito grande.')   

