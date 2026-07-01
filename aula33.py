""" Calculadora com While"""
from time import sleep

print('--'*30)
print('\033[1mESCOLHA DOIS VALORES E DIGITE A OPERAÇÃO QUE DESEJA REALIZAR\033[m')
print('--'*30)
print()
valor1 = float(input('Digite o primeiro valor: '))
valor2 = float(input('Digite o segundo valor: '))
print(f'Okay, você escolheu os valores {valor1} e {valor2}. Agora escolha a operação que deseja realizar: ')
sleep(1)
opcao = 0 

while opcao !=5
    print('''\033[1m[ 1 ] SOMA
-[ 2 ] SUBTRAÇÃO
-[ 3 ] MULTIPLICAÇÃO
-[ 4 ] DIVISÃO
-[ 5 ] SAIR\033[m''')
    opcao = int(input('Digite a opção desejada: '))
    if opcao == 1:
        print(f'A soma entre {valor1} e {valor2} é igual a: {valor1 + valor2}')
    elif opcao == 2:
        print(f'A subtração entre {valor1} e {valor2} é igual a: {valor1 - valor2}')
    if opcao == 3:
        print(f'A multiplicação entre {valor1} e {valor2} é igual a: {valor1 * valor2}')
    elif opcao == 4:
        if valor2 != 0:
            print(f'A divisão entre {valor1} e {valor2} é igual a: {valor1 / valor2}')
        else:
            print('Não é possível dividir por zero!')
    elif opcao == 5:
        print('Desligando calculadora...')
        sleep(1)
        break
print('Fim do programa!')