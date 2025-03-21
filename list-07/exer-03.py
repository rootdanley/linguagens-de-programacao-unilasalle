
dicionario = {
    'cachorro': 'dog',
    'gato': 'cat',
    'livro': 'book',
    'carro': 'car',
    'maçã': 'apple'
}


palavra = input("Digite uma palavra em português: ").strip().lower()


if palavra in dicionario:
    print(f"A tradução de '{palavra}' para o inglês é: '{dicionario[palavra]}'")
else:
    print(f"A tradução de '{palavra}' não foi encontrada no dicionário.")
