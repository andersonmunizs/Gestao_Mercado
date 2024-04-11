import Produto as pd
import Clientes as cl
import VendasCompras as vc

def menu_VendasCompras():
    while True:
        print("\n=== Menu Vendas e Compras ===")
        print("[1] Nova Venda")
        print("[2] Pesquisar compras pelo CPF")
        print("[3] Visualizar os 5 produtos mais vendidos ultimos 3 dias")
        print("[9] Retornar ao Menu Principal")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cpf_cliente = input("Digite o CPF do cliente: ")
            if len(cpf_cliente) == 14:
                vc.nova_venda(cpf_cliente)
            else:
                print("CPF inválido. Por favor, digite um CPF válido.")
        elif opcao == '2':
            cpf_consulta = input("Digite o CPF para a consulta: ")
            if len(cpf_consulta) == 14:
                vc.obter_informacoes_vendas_cpf(cpf_consulta)
        elif opcao == '3':
            vc.imprimir_itens_mais_vendidos_3_dias()
        elif opcao == '9':
            print("Voltando...\n")
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu_clientes():
    while True:
        print("\n=== Menu Clientes ===")
        print("[1] Cadastrar Novo Cliente")
        print("[2] Excluir Cliente")
        print("[3] Editar Cliente")
        print("[9] Voltar ao Menu Principal")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            listaClientes = cl.carregar_cliente() 
            cl.cadastrar_cliente(listaClientes)
        elif opcao == '2':
            listaClientes = cl.carregar_cliente()
            cpf_buscar = input("Digite o CPF do cliente a ser excluído: ")
            if len(cpf_buscar) == 14:
                cl.excluir_cliente(listaClientes, cpf_buscar)
            else:
                print("CPF inválido. Por favor, digite um CPF válido.")
        elif opcao == '3':
            cl.editar_cliente()
        elif opcao == '9':
            print("Voltando...\n")
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu_produto():
    listadeProdutos = pd.carregar_produto()
    while True:
        print("\n=== Menu Produto ===")
        print("[1] Cadastrar Produto")
        print("[2] Editar Produto")
        print("[3] Excluir Produto")
        print("[4] Verificar Estoque Baixo")
        print("[5] Quantidade de estoque por setor")
        print("[9] Voltar ao Menu Principal")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            pd.mostrar_produtos(listadeProdutos)
            pd.cadastrar_produto(listadeProdutos)
        elif opcao == '2':
            pd.mostrar_produtos(listadeProdutos)
            pd.editar_produto(listadeProdutos)
        elif opcao == '3':
            pd.mostrar_produtos(listadeProdutos)
            pd.excluir_produto(listadeProdutos)
        elif opcao == '4':
            limite_estoque_baixo = 50  # Pode ser um valor fixo ou obtido de outra forma, conforme sua necessidade
            pd.verifica_estoque_baixo(listadeProdutos, limite_estoque_baixo)
        elif opcao == '5':
            pd.calcular_estoque_por_setor()
        elif opcao == '9':
            print("Voltando...\n")
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu_principal():
    while True:
        print("\n### MENU PRINCIPAL ###")
        print("[1] Vendas e Compras")
        print("[2] Clientes")
        print("[3] Produtos")
        print("[9] Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            menu_VendasCompras()
        elif opcao == '2':
            menu_clientes()
        elif opcao == '3':
            menu_produto()
        elif opcao == '9':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")