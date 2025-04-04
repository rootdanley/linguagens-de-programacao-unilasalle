def main():
    entrada = input("Digite uma lista de palavras separadas por espaço: ")
    palavras = entrada.split()
    palavras_ordenadas = sorted(palavras, key=str.lower)
    print("Lista ordenada alfabeticamente:")
    print(palavras_ordenadas)
    print("\nNúmero total de palavras:")
    print(len(palavras))
    palavras_maiusculas = [palavra.upper() for palavra in palavras]
    print("\nPalavras em maiúsculas:")
    print(palavras_maiusculas)

if __name__ == "__main__":
    main()
