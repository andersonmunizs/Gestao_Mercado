import manipulaCSV as mcsv

def carregar_cliente() -> list:
    lista = mcsv.carregarDados("Cliente.csv")
    return lista

def cadastrar_cliente(listaClientes: list) -> bool:
    camposCliente = ["CPF", "Nome", "Nascimento", "Idade", "Endereço", "Cidade", "Estado", "Pontos"]
    cliente = {}
    for campo in camposCliente:
        if (campo != 'Pontos'):
            cliente[campo] = input(f"{campo}:")
        else:
            cliente[campo] = 0

    listaClientes.append(cliente)
    print(listaClientes)
    return mcsv.gravarDados('Cliente.csv', camposCliente, listaClientes)

def editar_cliente() -> bool:
    listaClientes = carregar_cliente()  # Corrigindo o nome da função
    cpf_cliente = input("Digite o CPF do cliente que deseja editar: ")
    campos = ["CPF", "Nome", "Nascimento", "Idade", "Endereço", "Cidade", "Estado", "Pontos"]

    # Verificando se o cliente está na lista
    cliente_encontrado = False
    for cliente in listaClientes:
        if cliente['CPF'] == cpf_cliente:
            cliente_encontrado = True
            print("Cliente encontrado:")
            print(cliente)
            print("=" * 20)

            print("Digite as novas informações do cliente:")
            for campo, valor_atual in cliente.items():
                novo_valor = input(f"{campo} ({valor_atual}): ").strip()
                if novo_valor:
                    cliente[campo] = novo_valor

            if mcsv.gravarDados("Cliente.csv", campos, listaClientes): 
                print("Cliente atualizado com sucesso.")
                return True
            else:
                print("Erro ao atualizar o cliente.")
                return False

    if not cliente_encontrado:
        print("Cliente não encontrado.")
        return False

def excluir_cliente(listaClientes: list, cpf: str) -> bool:
    flag = False
    camposCliente = list(listaClientes[0].keys())
    for i, cliente in enumerate(listaClientes):
        if cliente['CPF'] == cpf:
            flag = True
            listaClientes.pop(i)
    if flag:
        mcsv.gravarDados("Cliente.csv", camposCliente, listaClientes)
    return flag

