class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self):
        return f"Livro: {self.titulo} | Autor: {self.autor} | Páginas: {self.paginas}"

    def __len__(self):
        return self.paginas

def main():
    livro = Livro("Python para Iniciantes", "João Silva", 250)
    print(livro)
    print("Número de páginas:", len(livro))

if __name__ == "__main__":
    main()
