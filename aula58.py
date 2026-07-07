# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

# Crie uma função, fala se um número é par ou ímpar, retorne se o número é par ou ímpar.

def multiplica_argumentos(*args):
    total = 1
    for num in args:
        total *= num
    return total


multiplicacao = multiplica_argumentos(17, 2, 3)
print(multiplicacao)


def par_ou_impar(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "ímpar"
    

par_ou_impar_resultado = par_ou_impar(7)
print(par_ou_impar_resultado)