import meu_modulo

def main():
    try:
        num = float(input("Digite um número: "))
        print(f"O dobro de {num} é {meu_modulo.dobro(num)}")
    except ValueError:
        print("Por favor, digite um número válido.")

if __name__ == "__main__":
    main()
