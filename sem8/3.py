def main():
    while True:
        try:
            numero = int(input("Digite um número inteiro: "))
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")
            continue
        else:
            print(f"O dobro do número é: {numero * 2}")
            break

if __name__ == "__main__":
    main()
