import csv

 
def carregarDados( nomeArquivo: str) -> list : 
    try:
        arq = open(nomeArquivo, "r")
        listaClientes = csv.DictReader(arq, delimiter=';')
        listaClientes = list(listaClientes)
    except FileNotFoundError:
        print("Arquivo não encontrado ", nomeArquivo)
        return []
    return listaClientes


def gravarDados( nomeArquivo: str, campos : list, lista : list ) -> bool :
    try:
        # abrindo o arquivo a ser gravado para escrita(sobreescreve o existente)
        arq = open(nomeArquivo, "w", newline='')
        meuCSV = csv.DictWriter(arq,fieldnames=campos, delimiter=';')
        meuCSV.writeheader()        
        for r in lista:            
            meuCSV.writerow(r)
            print(r)
            arq.flush()
        arq.close()
        return True       
    except FileNotFoundError:
        print("erro na abertura do arquivo ", nomeArquivo)
        return False

