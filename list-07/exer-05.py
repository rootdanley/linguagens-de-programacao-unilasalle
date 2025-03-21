
produtos = {
    101: ("Camiseta", 29.90),
    102: ("Calça Jeans", 89.90),
    103: ("Tênis", 199.90),
    104: ("Jaqueta", 129.90),
    105: ("Bolsa", 69.90)
}


codigo = int(input("Digite o código do produto: "))


if codigo in produtos:
    nome, preco = produtos[codigo]
    print(f"\nProduto: {nome}")
    print(f"Preço: R${preco:.2f}")
else:
    print("\nCódigo de produto não encontrado.")
