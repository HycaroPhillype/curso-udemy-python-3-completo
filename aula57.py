"""

args - Argumento não nomeados
* - *args (empacotamento e desempacotamento)

"""

# Lembre-te de desempacotamento.

# x, y, *resto = 1, 2, 3, 4, 5, 6
# print(x, y, resto)

# def soma(x, y ):
#     return x + y

def soma(*args):
    total = 0
    for numero in args:
        total += numero
    return total

soma1 = soma(1, 2, 3, 4, 5)
print(soma1)

numeros = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
soma2 = soma(*numeros)
print(soma2)

print(sum(numeros))  # Função built-in do Python