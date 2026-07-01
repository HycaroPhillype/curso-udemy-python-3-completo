nome = str(input('Digite o nome: ')) 
altura = float(input('Digite a altura: '))
peso = float(input('Digite o peso: '))
imc = peso / (altura ** 2)

print(f'Nome: {nome.strip()}')
print(f'Altura: {altura}')
print(f'Peso: {peso}')
print(f'IMC: {imc:.2f}')

if imc < 18.5:
    print('Classificação: Abaixo do peso')
elif 18.5 <= imc < 25:
    print('Classificação: Peso normal')
elif 25 <= imc < 30:
    print('Classificação: Sobrepeso')
else:    print('Classificação: Obesidade')  


# if / elif      / else
# se / se não se / se não

condicao1 = True
condicao2 = True
condicao3 = True
condicao4 = True

if condicao1:
    print('Código para condição 1')
    print('Código para condição 1')
elif condicao2:
    print('Código para condição 2')
elif condicao3:
    print('Código para condição 3')
elif condicao4:
    print('Código para condição 4')
else:
    print('Nenhuma condição foi satisfeita.')

if 10 == 10:
    print('Outro if')

print('Fora do if')