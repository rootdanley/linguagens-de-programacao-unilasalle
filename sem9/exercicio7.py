class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def exibir_detalhes(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}")

def main():
    carro1 = Carro("Toyota", "Corolla", 2020)
    carro2 = Carro("Honda", "Civic", 2021)
    print("Detalhes do carro 1:")
    carro1.exibir_detalhes()
    print("\nDetalhes do carro 2:")
    carro2.exibir_detalhes()

if __name__ == "__main__":
    main()
