def multiplicador(fator):
    def multiplicar(n):
        return n * fator
    return multiplicar

def main():
    try:
        fator = float(input("Digite o fator: "))
        num = float(input("Digite um número para multiplicar: "))
        mult = multiplicador(fator)
        print(f"O resultado de {num} x {fator} é {mult(num)}")
    except ValueError:
        print("Por favor, digite números válidos.")

if __name__ == "__main__":
    main()
