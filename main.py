# Sistema simples de controle de estoque
# Projeto desenvolvido em Python

estoque = {}


def cadastrar_produto():
    codigo = input("Digite o código do produto: ")
    nome = input("Digite o nome do produto: ")
    quantidade = int(input("Digite a quantidade inicial: "))
    preco = float(input("Digite o preço do produto: "))

    estoque[codigo] = {
        "nome": nome,
        "quantidade": quantidade,
        "preco": preco
    }

    print("Produto cadastrado com sucesso!")


def entrada_estoque():
    codigo = input("Digite o código do produto: ")

    if codigo in estoque:
        quantidade = int(input("Quantidade de entrada: "))
        estoque[codigo]["quantidade"] += quantidade
        print("Estoque atualizado!")
    else:
        print("Produto não encontrado.")


def saida_estoque():
    codigo = input("Digite o código do produto: ")

    if codigo in estoque:
        quantidade = int(input("Quantidade de saída: "))

        if quantidade <= estoque[codigo]["quantidade"]:
            estoque[codigo]["quantidade"] -= quantidade
            print("Saída registrada!")
        else:
            print("Quantidade insuficiente no estoque.")
    else:
        print("Produto não encontrado.")


def gerar_relatorio():
    print("\n===== RELATÓRIO DE ESTOQUE =====")

    if len(estoque) == 0:
        print("Nenhum produto cadastrado.")
        return

    valor_total_estoque = 0

    for codigo, produto in estoque.items():
        total_produto = produto["quantidade"] * produto["preco"]
        valor_total_estoque += total_produto

        print("-----------------------------")
        print("Código:", codigo)
        print("Produto:", produto["nome"])
        print("Quantidade:", produto["quantidade"])
        print("Preço: R$", produto["preco"])
        print("Valor em estoque: R$", total_produto)

    print("-----------------------------")
    print("Valor total do estoque: R$", valor_total_estoque)


def menu():
    while True:
        print("\n===== CONTROLE DE ESTOQUE =====")
        print("1 - Cadastrar produto")
        print("2 - Entrada de produto")
        print("3 - Saída de produto")
        print("4 - Gerar relatório")
        print("5 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_produto()

        elif opcao == "2":
            entrada_estoque()

        elif opcao == "3":
            saida_estoque()

        elif opcao == "4":
            gerar_relatorio()

        elif opcao == "5":
            print("Sistema encerrado.")
            break

        else:
            print("Opção inválida.")


menu()