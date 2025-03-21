
cores_arco_iris = ("Vermelho", "Laranja", "Amarelo", "Verde", "Azul", "Anil", "Violeta")


numero = int(input("Informe um número de 1 a 7 para saber a cor correspondente: "))


if 1 <= numero <= 7:
    
    print(f"A cor correspondente ao número {numero} é: {cores_arco_iris[numero - 1]}")
else:
    print("Número inválido! Informe um número de 1 a 7.")
