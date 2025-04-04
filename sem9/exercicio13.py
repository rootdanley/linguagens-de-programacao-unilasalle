import os

def main():
    # Verifica se o arquivo "dados.txt" existe; se não, cria um com conteúdo padrão.
    if not os.path.exists("dados.txt"):
        with open("dados.txt", "w", encoding="utf-8") as file:
            file.write("Esta é a linha 1.\nEsta é a linha 2.\nEsta é a linha 3.\n")
        print("Arquivo 'dados.txt' não encontrado. Um arquivo de exemplo foi criado.\n")
    
    try:
        with open("dados.txt", "r", encoding="utf-8") as file:
            linhas = file.readlines()
            print(f"O arquivo 'dados.txt' possui {len(linhas)} linhas.")
            print("Conteúdo do arquivo:")
            for linha in linhas:
                print(linha, end="")
    except Exception as e:
        print("Ocorreu um erro:", e)

if __name__ == "__main__":
    main()
