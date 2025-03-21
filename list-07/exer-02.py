palavra = input("Digite uma palavra: ")


contagem = {}


for caractere in palavra:
    if caractere in contagem:
        contagem[caractere] += 1  
    else:
        contagem[caractere] = 1 

print("\nContagem de caracteres:")
print(contagem)
