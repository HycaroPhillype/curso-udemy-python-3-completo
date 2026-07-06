"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados.
"""

# x = 1


# def escopo():
#     global x
#     x = 10

#     def outra_funcao():
#         global x
#         x = 11
#         y = 2
#         print(x, y)

#     outra_funcao()
#     print(x)


# print(x)
# escopo()
# print(x)

"""
Retorno de valores das funções (return)
"""


def soma(x, y):
    if x > 10:
        return [10, 20]
    return x + y


# variavel = soma(1, 2)
# variavel = int('1')
soma1 = soma(2, 2)
soma2 = soma(3, 3)
print(soma1)
print(soma2)
print(soma(11, 55))

