import manipulaCSV as mcsv

def carregar_produto() -> list: #Carregando o arquivo Produtos.csv
    listaProdutos = mcsv.carregarDados("Produtos.csv")
    return listaProdutos

def print_produtos(listaProdutos):
    print("{:<3} {:<10} {:<15} {:<7} {:<10} {:<10}".format("ID", "Setor", "Nome", "Preço", "Validade", "Quantidade"))
    print("_" * 66)  # Linha divisória
    for product in listaProdutos:
        print("{:<3} {:<10} {:<15} {:<7} {:<10} {:<10}".format(product["Id"], product["Setor"], product["Nome"], product["Preco"], product["Validade"], product["Quantidade"]))
    print() # \n

def cadastrarProduto():
    print("==== Cadastro de produto ====")
    produto = {}
    produto['Id'] = input("ID do produto: ")
    
    while True:
        setor = input("Setor do produto: [Higiene, Limpeza, Bebidas, Frios, Padaria, Açougue]\n")
        if setor.lower() in ['higiene', 'limpeza', 'bebidas', 'frios', 'padaria', 'açougue']:
            produto['Setor'] = setor.title()  # Converte para título caso o usuário digite em minúsculas
            break
        else:
            print("Por favor, digite um setor válido.")

    produto['Nome'] = input("Nome do produto: ")
    produto['Preco'] = float(input("Preço do produto: "))
    produto['Validade'] = input("Data de validade do produto: ")
    produto['Quantidade'] = int(input("Quantidade de produto no estoque: "))
    print("Produto cadastrado com sucesso!\n\n")
    return produto

def cadastrar_produto(listaProdutos: list) -> bool:
    prod = cadastrarProduto()
    listaProdutos.append(prod)
    campos = ["Id", "Setor", "Nome", "Preco", "Validade", "Quantidade"]
    return mcsv.gravarDados("Produtos.csv", campos, listaProdutos)


def editar_produto(listaProdutos: list) -> None:
    id_produto = input("Digite o ID do produto que deseja editar: ")

    #Verificando se o produto está na lista
    produto_encontrado = False
    for produto in listaProdutos:
        if produto['Id'] == id_produto:
            produto_encontrado = True
            print("Produto encontrado:")
            print(produto)
            print("-" * 30)

            print("Digite as novas informações do produto:")
            novo_produto = {}
            for campo, valor_atual in produto.items():
                novo_valor = input(f"{campo} ({valor_atual}): ").strip()
                if novo_valor:
                    novo_produto[campo] = novo_valor
                else:
                    novo_produto[campo] = valor_atual

            # Atualizando o produto na lista
            index_produto = listaProdutos.index(produto)
            listaProdutos[index_produto] = novo_produto

            # Registrando os produtos atualizados no arquivo CSV
            campos = ["Id", "Setor", "Nome", "Preco", "Validade", "Quantidade"]
            mcsv.gravarDados("Produtos.csv", campos, listaProdutos)

            print("Produto editado com sucesso.")
            break
    if not produto_encontrado:
        print("Produto não encontrado.")


def excluir_produto(listaProdutos: list) -> bool:
    id_produto = input("Digite o ID do produto que deseja excluir: ")
    produto_encontrado = False
    for produto in listaProdutos:
        if produto['Id'] == id_produto:
            produto_encontrado = True
            print("Produto encontrado:")
            print(produto)
            print("-" * 30)

            certeza = input("Tem certeza que deseja excluir o produto? (S/N): ").strip().upper()
            if certeza == "S":
                listaProdutos.remove(produto)

                campos = ["Id", "Setor", "Nome", "Preco", "Validade", "Quantidade"]
                return mcsv.gravarDados("Produtos.csv", campos, listaProdutos)

    if not produto_encontrado:
        print("Produto não encontrado.")
        return False

def verifica_estoque_baixo(limite_estoque_baixo: int) -> list:
    listaProdutos = mcsv.carregarDados("Produtos.csv")
    produtos_estoque_baixo = []

    for produto in listaProdutos:

        if int(produto['Quantidade']) < limite_estoque_baixo:
            produtos_estoque_baixo.append(produto)

    if produtos_estoque_baixo:
        print("Os seguintes produtos estão com estoque baixo:")
        for produto in produtos_estoque_baixo:
            print(produto)
    else:
        print("Nenhum produto está com estoque baixo.")

    return listaProdutos

import csv

def calcular_estoque_por_setor():
    estoque_setor = {}

    with open('Produtos.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader:
            setor = row['Setor']
            quantidade = int(row['Quantidade'])
            if setor in estoque_setor:
                estoque_setor[setor] += quantidade
            else:
                estoque_setor[setor] = quantidade

    #Mostrando
    print("Quantidade de estoque por setor:")
    for setor, estoque in estoque_setor.items():
        print(f"{setor}: {estoque}")