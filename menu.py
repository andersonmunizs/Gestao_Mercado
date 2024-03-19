import cliente as cl
import manipulaCSV as mcsv

def menuPrincipal():
    while True:
        print("====Menu Principal====")
        print("[1] Venda\n[2] Clientes\n[3] Produtos\n[9] Sair")

        escolha = input("Digite a opção desejada:")

        if escolha == "1":
            menuVenda()
        elif escolha == "2":
            menuCliente()
        elif escolha == "3":
            menuProduto()
        elif escolha == "9":
            print("Saindo...")
            break
        else:
            print("\nOpção Inválida. Tente novamente")


def menuVenda(): # FALTA IMPLEMENTAR
    print("====Venda====\n[1] Nova Venda\n[2] Listar Vendas dos Clientes\n[9] Voltar")

    escolha = input("\nDigite a opção desejada:")

    if escolha == "1": # FALTA IMPLEMENTAR
        print("")
    elif escolha == "2": # FALTA IMPLEMENTAR
        print("")
    elif escolha == "9":
        print("Voltando...")
    else:
        print("\nOpção Inválida. Tente novamente")

def menuCliente():
    print("====Cliente====\n[1] Cadastrar novo cliente\n[2] Atualizar pontuação\n[3] Atualizar cliente\n[9] Voltar")

    escolha = input("\nDigite a opção desejada:")

    if escolha == "1": # PRONTO
        listaClientes = cl.carregarCliente()  
        cl.cadastrarCliente(listaClientes)  
    elif escolha == "2": # FALTA IMPLEMENTAR
        print("")
    elif escolha == "3": # FALTA IMPLEMENTAR
        print("")
    elif escolha == "9": 
        print("")
    else:
        print("\nOpção Inválida. Tente novamente")

def menuProduto(): # FALTA IMPLEMENTAR
    print("[1] Cadastrar novo produto\n[2] Atualizar informações do produto\n[3] Estoque por setor\n[4] Produtos com estoque baixo\n[5] Produtos mais vendidos")

    escolha = input("\n Digite a opção desejada:")

    if escolha == "1": # FALTA IMPLEMENTAR
        print("")
    elif escolha == "2": # FALTA IMPLEMENTAR
        print("")
    elif escolha == "3": # FALTA IMPLEMENTAR
        print("")
    elif escolha == "4": # FALTA IMPLEMENTAR
        print("")
    elif escolha == "5": # FALTA IMPLEMENTAR
        print("")
    elif escolha == "9":
        print("Voltando...")
    else:
        print("\nOpção Inválida. Tente novamente")