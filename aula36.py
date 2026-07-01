# senha_salva = '123456'
# senha_digitada = ''
# repeticoes = 0

# while senha_salva != senha_digitada:
#     senha_digitada = input(f'Sua senha ({repeticoes}x): ')

#     repeticoes += 1

# print(repeticoes)
# print('Aquele laço acima pode ter repetições infinitas')



# LAÇO DE REPETIÇÃO COM FOR 


# texto = 'Python'

# novo_texto = ''
# for letra in texto:
#     novo_texto += f'*{letra}'
#     print(letra)
# print(novo_texto + '*')

"""
For + Range
range -> range(start, stop, step)
"""
# numeros = range(0, 100, 8)

# for numero in numeros:
#     print(numero)

"""
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""
# for letra in texto
# texto = 'Luiz'  # iterável

# # iteratador = iter(texto)  # iterator

# # while True:
# #     try:
# #         letra = next(iteratador)
# #         print(letra)
# #     except StopIteration:
# #         break

# for letra in texto:
#     print(letra)


for i in range(10):
    if i == 2:
        print('i é 2, pulando...')
        continue

    if i == 8:
        print('i é 8, seu else não executará')
        break

    for j in range(1, 3):
        print(i, j)
else:
    print('For completo com sucesso!')