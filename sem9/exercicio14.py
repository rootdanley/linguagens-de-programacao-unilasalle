import pickle

def main():
    numeros = [1, 2, 3, 4, 5]
    # Escrevendo a lista no arquivo binário
    try:
        with open("dados.bin", "wb") as file:
            pickle.dump(numeros, file)
        print("Números escritos no arquivo 'dados.bin'.")
    except Exception as e:
        print("Erro ao escrever no arquivo:", e)
        return

    # Lendo os números do arquivo binário
    try:
        with open("dados.bin", "rb") as file:
            numeros_lidos = pickle.load(file)
        print("Números lidos do arquivo 'dados.bin':")
        print(numeros_lidos)
    except Exception as e:
        print("Erro ao ler o arquivo:", e)

if __name__ == "__main__":
    main()
