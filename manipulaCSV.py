import csv
import os

def carregarDados(nomeArquivo: str) -> list:
    try:
        with open(nomeArquivo, "r", encoding="utf-8") as arq:
            listaClientes = list(csv.DictReader(arq, delimiter=';'))
    except FileNotFoundError as e:
        print(f"Erro: Arquivo não encontrado: {e.filename}")
        return []
    except Exception as e:
        print(f"Erro inesperado ao carregar dados: {e}")
        return []
    return listaClientes

def gravarDados(nomeArquivo: str, campos: list, lista: list, modo: str = "w") -> bool:
    try:
        arquivo_existe = os.path.isfile(nomeArquivo)
        with open(nomeArquivo, modo, newline='', encoding='utf-8') as arq:
            meuCSV = csv.DictWriter(arq, fieldnames=campos, delimiter=';')

            if modo == "w" or not arquivo_existe:
                meuCSV.writeheader()
            for r in lista:
                meuCSV.writerow(r)
            arq.flush()

        return True
    except FileNotFoundError as e:
        print(f"Erro: Arquivo não encontrado: {e.filename}")
        return False
    except Exception as e:
        print(f"Erro inesperado ao gravar dados: {e}")
        return False


