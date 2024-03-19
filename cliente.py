import manipulaCSV as mcsv


def carregarCliente() ->list: 
    
    lista = mcsv.carregarDados("Cliente.csv")
    return lista
    

def cadastrarCliente( listaClientes : list ) -> bool :
    
    camposCliente = ["CPF","Nome","Nascimento","Idade","Endereço","Cidade","Estado","Pontos"]
    cliente = {}
    for campo in camposCliente:
        if (campo != 'Pontos'):
            cliente[campo] = input(f"{campo}:")
        else:
            cliente[campo] =  0            
        
    listaClientes.append(cliente)
    print(listaClientes)
    return mcsv.gravarDados('Cliente.csv', camposCliente, listaClientes )

def excluirCliente(listaClientes : list, cpf : str ) -> bool:

    flag = False
    camposCliente = list(listaClientes[0].keys())
    for i,cliente in enumerate(listaClientes):
        if cliente['CPF'] ==  cpf :
            flag = True
            listaClientes.pop(i)
    #print(listaClientes)
    if flag:
        mcsv.gravarDados("Cliente.csv", camposCliente, listaClientes)
    return flag
    
    
            
    