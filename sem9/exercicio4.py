def contar_vogais(frase):
    vogais = "aeiouAEIOU"
    contagem = {}
    for v in vogais:
        contagem[v] = frase.count(v)
    return contagem

def main():
    frase = input("Digite uma frase: ")
    contagem = contar_vogais(frase)
    print("Contagem de vogais:")
    for vogal, quantidade in contagem.items():
        if quantidade > 0:
            print(f"{vogal}: {quantidade}")
    print("\nFrase invertida:")
    print(frase[::-1])
    print("\nFrase com espaços substituídos por '-':")
    print(frase.replace(" ", "-"))

if __name__ == "__main__":
    main()
