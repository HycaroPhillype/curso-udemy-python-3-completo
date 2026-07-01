"""
FAÇA UMA LISA DE COMPRAR COM LISTAS 
O USUÁRIO DEVE TER A POSSIBILIDADE DE ADICIONAR, REMOVER E VISUALIZAR OS ITENS DA LISTA DE COMPRAS.
NÃO PERMITA QUE O PROGRAMA COM ERROS DE ÍNDICES INEXISTENTES NA LISTA. 
"""

listas_compras = []

while True:
    # print("\nLista de Compras:")
    # for i, item in enumerate(listas_compras):
    #     print(f"{i + 1}. {item}")
    print("\nLista de Compras:")
    print("------------------")
    print('[1] Adicionar item\n' \
    '[2] Remover item\n' \
    '[3] Visualizar lista\n' \
    '[4] Sair')
    # print("1. Adicionar item")
    # print("2. Remover item")
    # print("3. Visualizar lista")
    # print("4. Sair")

    escolha = input("Escolha uma opção (1-4): ")

    if escolha == "1":
        item = input("Digite o item que deseja adicionar: ")
        listas_compras.append(item)
        print(f"{item} adicionado à lista de compras.")
    
    elif escolha == "2":
        if not listas_compras:
            print("A lista de compras está vazia. Não há itens para remover.")
            continue
        
        try:
            indice = int(input("Digite o número do item que deseja remover: ")) - 1
            if 0 <= indice < len(listas_compras):
                removido = listas_compras.pop(indice)
                print(f"{removido} removido da lista de compras.")
            else:
                print("Índice inválido. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido.")
    
    elif escolha == "3":
        if not listas_compras:
            print("A lista de compras está vazia.")
        else:
            print("\nItens na lista de compras:")
            for i, item in enumerate(listas_compras):
                print(f"{i + 1}. {item}")
    
    elif escolha == "4":
        print("Saindo do programa...")
        break
    
    else:
        print("Opção inválida. Por favor, escolha uma opção entre 1 e 4.")