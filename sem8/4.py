def main():
    lista = [10, 20, 30, 40, 50]
    try:
        indice = int(input("Digite um índice (0 a 4) para acessar um valor da lista: "))
        elemento = lista[indice]
    except ValueError:
        print("Erro: Entrada inválida. Por favor, digite um número inteiro.")
    except IndexError:
        print("Erro: Índice inválido. Por favor, digite um índice entre 0 e 4.")
    else:
        print(f"O elemento no índice {indice} é: {elemento}")

if __name__ == "__main__":
    main()
