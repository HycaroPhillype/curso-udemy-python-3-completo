"""
Valores padrão para parâmetros
Ao definir uma função, os parâmetros podem
ter valores padrão. Caso o valor não seja
enviado para o parâmetro, o valor padrão será
usado.
Refatorar: editar o seu código.
"""


# OBS: OS parâmetros com valores padrão devem ser sempre os últimos da lista de parâmetros. Ou seja, não podemos ter um parâmetro com valor padrão antes de um parâmetro sem valor padrão.
# def soma(x, y, z=None):
#     if z is not None:
#         print(f'{x=} {y=} {z=}', x + y + z)
#     else:
#         print(f'{x=} {y=}', x + y)


# soma(1, 2)
# soma(3, 5)
# soma(100, 200)
# soma(7, 9, 0)
# soma(y=9, z=0, x=7)

def function(a, b, c='Hycaro'):
    if c is not None:
        return f'{a=} {b=} {c=}', a + b + len(c)
    
print(function(1, 2))