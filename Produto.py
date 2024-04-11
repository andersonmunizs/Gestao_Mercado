import manipulaCSV as mcsv
import csv
import sys

def carregar_produto() -> list:
    try:
        listadeProdutos = mcsv.carregarDados("Produtos.csv")
        return listadeProdutos
    except FileNotFoundError:
        print("Arquivo 'Produtos.csv' não encontrado.")
        sys.exit(1)

def mostrar_produtos(listadeProdutos):
    print("{:<4} {:<9} {:<20} {:<6} {:<11} {:<10}".format("[ID]", "[Setor]", "[Nome]", "[Preço]", "[Validade]", "[Quantidade]"))
    for product in listadeProdutos:
        nome_formatado = product["Nome"][:15] if len(product["Nome"]) > 15 else product["Nome"]
        print("{:<4} {:<9} {:<20} {:<6} {:<11} {:<10}".format(product["Id"], product["Setor"], nome_formatado, product["Preco"], product["Validade"], product["Quantidade"]))
    print() # \n

def input_cadastrar_Produto():
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

def cadastrar_produto(listadeProdutos: list) -> bool:
    prod = input_cadastrar_Produto()
    listadeProdutos.append(prod)
    campos = ["Id", "Setor", "Nome", "Preco", "Validade", "Quantidade"]
    return mcsv.gravarDados("Produtos.csv", campos, listadeProdutos)


def editar_produto(listadeProdutos: list) -> None:
    id_produto = input("Digite o ID do produto que deseja editar: ")
    produto_encontrado = False

    for produto in listadeProdutos:
        if produto['Id'] == id_produto:
            produto_encontrado = True
            print("Produto encontrado:")
            print(produto)
            print("=" * 30)

            print("Edite as novas informações do produto:")
            novo_produto = {}
            for campo, valor_atual in produto.items():
                novo_valor = input(f"{campo} ({valor_atual}): ").strip()
                if campo == 'Preco':
                    while True:
                        try:
                            novo_valor = float(novo_valor)
                            if novo_valor >= 0:
                                break
                            else:
                                print("O preço deve ser um número positivo.")
                                novo_valor = input(f"{campo} ({valor_atual}): ").strip()
                        except ValueError:
                            print("Por favor, digite um preço válido.")
                            novo_valor = input(f"{campo} ({valor_atual}): ").strip()
                elif campo == 'Quantidade':
                    while True:
                        try:
                            novo_valor = int(novo_valor)
                            if novo_valor >= 0:
                                break
                            else:
                                print("A quantidade deve ser um número inteiro não negativo.")
                                novo_valor = input(f"{campo} ({valor_atual}): ").strip()
                        except ValueError:
                            print("Por favor, digite uma quantidade válida.")
                            novo_valor = input(f"{campo} ({valor_atual}): ").strip()

                if novo_valor:
                    novo_produto[campo] = novo_valor
                else:
                    novo_produto[campo] = valor_atual

            index_produto = listadeProdutos.index(produto)
            listadeProdutos[index_produto] = novo_produto
            campos = ["Id", "Setor", "Nome", "Preco", "Validade", "Quantidade"]
            try:
                mcsv.gravarDados("Produtos.csv", campos, listadeProdutos)
                print("Produto editado com sucesso.")
            except Exception as e:
                print("Erro ao salvar as alterações no arquivo:", e)

            break

    if not produto_encontrado:
        print("Produto não encontrado.")


def excluir_produto(listadeProdutos: list) -> bool:
    id_produto = input("Digite o ID do produto que deseja excluir: ")
    produto_encontrado = False
    for produto in listadeProdutos:
        if produto['Id'] == id_produto:
            produto_encontrado = True

            print("Produto encontrado:")
            print(produto)
            print("=" * 30)

            certeza = input("Certeza ao excluir o produto? (S/N): ").strip().upper()
            if certeza == "S":
                listadeProdutos.remove(produto)
                campos = ["Id", "Setor", "Nome", "Preco", "Validade", "Quantidade"]
                return mcsv.gravarDados("Produtos.csv", campos, listadeProdutos)

    if not produto_encontrado:
        print("Produto não encontrado.")
        return False

def verifica_estoque_baixo(listadeProdutos: list, limite_estoque_baixo: int) -> None:
    produtos_estoque_baixo = []

    for produto in listadeProdutos:
        if int(produto['Quantidade']) < limite_estoque_baixo:
            produtos_estoque_baixo.append(produto)

    if produtos_estoque_baixo:
        print(f"Os seguintes produtos estão com estoque baixo (menos do que {limite_estoque_baixo}):")
        for produto in produtos_estoque_baixo:
            print(produto)
    else:
        print("Nenhum produto está com estoque baixo.")

    return listadeProdutos

def calcular_estoque_por_setor():
    try:
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
    except FileNotFoundError:
        print("Arquivo 'Produtos.csv' não encontrado.")
        sys.exit(1)