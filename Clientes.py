import manipulaCSV as mcsv

def carregar_cliente() -> list:
    try:
        return mcsv.carregarDados("Cliente.csv")
    except FileNotFoundError:
        print("Arquivo de clientes não encontrado.")
        return []

def cadastrar_cliente(listaClientes: list) -> bool:
    try:
        campos_cliente = ["CPF", "Nome", "Nascimento", "Idade", "Endereço", "Cidade", "Estado", "Pontos"]
        cliente = {}
        for campo in campos_cliente:
            if campo != 'Pontos':
                cliente[campo] = input(f"{campo}: ")
            else:
                cliente[campo] = 0

        listaClientes.append(cliente)
        return mcsv.gravarDados('Cliente.csv', campos_cliente, listaClientes)
    except IOError:
        print("Erro ao acessar o arquivo de clientes.")
        return False

def editar_cliente() -> bool:
    try:
        listaClientes = carregar_cliente()  
        cpf_cliente = input("Digite o CPF do cliente que deseja editar: ")
        campos = ["CPF", "Nome", "Nascimento", "Idade", "Endereço", "Cidade", "Estado", "Pontos"]

        cliente_encontrado = False
        for cliente in listaClientes:
            if cliente['CPF'] == cpf_cliente:
                cliente_encontrado = True
                print("Cliente encontrado:")
                print(cliente)

                print("Digite as novas informações do cliente:")
                for campo, valor_atual in cliente.items():
                    novo_valor = input(f"{campo} ({valor_atual}): ").strip()
                    if novo_valor:
                        cliente[campo] = novo_valor

                if mcsv.gravarDados("Cliente.csv", campos, listaClientes): 
                    print("Cliente editado com sucesso.")
                    return True
                else:
                    print("Erro ao editar o cliente.")
                    return False

        if not cliente_encontrado:
            print("Cliente não encontrado.")
            return False
    except IOError:
        print("Erro ao acessar o arquivo de clientes.")
        return False

def excluir_cliente(listaClientes: list, cpf: str) -> bool:
    try:
        flag = False
        campos_cliente = list(listaClientes[0].keys())
        for i, cliente in enumerate(listaClientes):
            if cliente['CPF'] == cpf:
                flag = True
                listaClientes.pop(i)
        if flag:
            mcsv.gravarDados("Cliente.csv", campos_cliente, listaClientes)
        return flag
    except IOError:
        print("Erro ao acessar o arquivo de clientes.")
        return False

