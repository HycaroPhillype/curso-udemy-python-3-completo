from time import sleep
import os
"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
palavra_secreta =  'casa'
letras_acertadas = ''
tentativas = 0
while True:
    escolha_letra = input('Digite uma letra: ')
    tentativas += 1
    if len(escolha_letra) > 1:
        print('Digite apenas uma letra.')
        sleep(1)
        continue

    if escolha_letra in palavra_secreta:
        letras_acertadas += escolha_letra
    palavra_formada = ''
    for letra in palavra_secreta:
        if letra in letras_acertadas:
            palavra_formada += letra
        else:
            palavra_formada += '*'

    print('Palavra formada: ',palavra_formada)
    sleep(1)
        

    if palavra_formada == palavra_secreta:
        os.system('cls')
        print('PARABÉNS! Você acertou a palavra secreta!')
        sleep(1)
        print('A palavra secreta é: ', palavra_secreta)
        sleep(1)
        print('Você precisou de ', tentativas, 'tentativas para acertar a palavra secreta.')
        break


