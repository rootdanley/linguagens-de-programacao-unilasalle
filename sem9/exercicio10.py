def contar_pares(n):
    for num in range(2, n + 1, 2):
        yield num

def main():
    try:
        limite = int(input("Digite um valor inteiro: "))
        print(f"Números pares até {limite}:")
        for par in contar_pares(limite):
            print(par, end=" ")
        print()
    except ValueError:
        print("Por favor, digite um número inteiro válido.")

if __name__ == "__main__":
    main()
