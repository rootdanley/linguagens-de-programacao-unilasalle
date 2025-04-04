class Animal:
    def fazer_som(self):
        print("Som de animal")

class Cachorro(Animal):
    def fazer_som(self):
        print("Au Au")

class Gato(Animal):
    def fazer_som(self):
        print("Miau")

def main():
    animal = Animal()
    cachorro = Cachorro()
    gato = Gato()

    print("Animal:")
    animal.fazer_som()
    print("\nCachorro:")
    cachorro.fazer_som()
    print("\nGato:")
    gato.fazer_som()

if __name__ == "__main__":
    main()
