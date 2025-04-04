def main():
    nome_arquivo = input("Digite o nome do arquivo para leitura: ")
    try:
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read()
            print("Conteúdo do arquivo:")
            print(conteudo)
    except FileNotFoundError:
        print("Erro: Arquivo não encontrado.")
    except Exception as e:
        print("Erro ao abrir o arquivo:", e)

if __name__ == "__main__":
    main()
