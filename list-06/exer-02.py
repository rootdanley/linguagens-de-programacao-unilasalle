
numeros = tuple(int(input(f"Digite o {i+1}º número inteiro: ")) for i in range(4))


quantidade_nove = numeros.count(9)


if 3 in numeros:
    posicao_tres = numeros.index(3)
else:
    posicao_tres = "Não existe o número 3"


pares = [num for num in numeros if num % 2 == 0]


print(f"\nA quantidade de vezes que o número 9 apareceu: {quantidade_nove}")
print(f"A posição do primeiro número 3 (caso exista): {posicao_tres}")
print(f"Os números pares na tupla são: {pares}")
