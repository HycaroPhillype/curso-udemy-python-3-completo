# Exercício - sistema de perguntas e respostas
from time import sleep

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
    {
        'Pergunta': 'Quanto é 15-10?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

letras = ['A', 'B', 'C', 'D']
contador = 0

# Linha em branco para separar as perguntas
for pergunta in perguntas:
    print('Pergunta:', pergunta['Pergunta'])
    print('Opções:')


    for indice, opcao in enumerate(pergunta['Opções']):
        print(f'{letras[indice]}) {opcao}')

    resposta_usuario = input('Digite sua resposta: ').upper()

    indice_resposta = letras.index(resposta_usuario)
    resposta_correta = pergunta['Opções'][indice_resposta]


    if resposta_correta == pergunta['Resposta']:
        print(f'Você escolheu: {resposta_correta}')
        print('Resposta correta!')
        contador += 1
    else:
        print(f'Você escolheu: {resposta_correta}')
        print('Resposta incorreta. A resposta correta é:', pergunta['Resposta'])

    
    print()  # Linha em branco para separar as perguntas

print('Você acertou', contador, 'pergunta(s) de', len(perguntas))







# print('Bem-vindo ao sistema de perguntas e respostas!')
# print('Responda às perguntas abaixo:')
# print() 

# print('Pergunta 1: Quanto é 2+2?')
# print()
# print('Opções:')
# print()

# print(
#     '0) 1\n' 
#     '1) 3\n' \
#     '2) 4\n' \
#     '3) 5\n' \
# ) 
# resposta_usuario = input('Digite sua resposta: ')
# if resposta_usuario == perguntas[0]['Resposta']:
#     print('Resposta correta!')
# else:
    # print('Resposta incorreta. A resposta correta é:', perguntas[0]['Resposta'])
