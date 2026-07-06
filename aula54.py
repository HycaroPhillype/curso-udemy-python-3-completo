"""

INTRODUÇÃO AS FUNÇÕES (def) em Python
Funções são trechos de código usados para replicar determinada 
ação ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos) e retornar um valor especifico.
Por padrão, funções Python retornam None (nada).

"""

# def soma(a, b):
#     """Função que recebe dois valores e retorna a soma deles"""
#     return a + b

# # Exemplo de uso da função
# resultado = soma(5, 3)
# print(resultado)  # Saída: 8    

# def multiplo_de(numero, multiplo):
#     resultado = numero % multiplo == 0
#     print(f'{numero} é múltiplo de {multiplo}?', end=' ')
#     print(resultado)
 
 
# multiplo_de(16, 8)
# multiplo_de(15, 3)
# multiplo_de(10, 2)

"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""


def soma(x, y, z):
    # Definição
    print(f'{x=} y={y} {z=}', '|', 'x + y + z = ', x + y + z)


soma(1, 2, 3)
soma(1, y=2, z=5)

print(1, 2, 3, sep='-')