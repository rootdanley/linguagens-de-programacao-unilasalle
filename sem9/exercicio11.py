class Contador:
    def __init__(self, n):
        self.n = n
        self.atual = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.atual <= self.n:
            numero = self.atual
            self.atual += 1
            return numero
        else:
            raise StopIteration

def main():
    try:
        limite = int(input("Digite o valor de n: "))
        print(f"Contagem de 1 até {limite}:")
        for num in Contador(limite):
            print(num, end=" ")
        print()
    except ValueError:
        print("Por favor, digite um número inteiro válido.")

if __name__ == "__main__":
    main()
