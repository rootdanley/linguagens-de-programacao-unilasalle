import math
import random

def main():
    try:
        num = float(input("Digite um número: "))
        raiz = math.sqrt(num)
        print(f"A raiz quadrada de {num} é {raiz}")
    except ValueError:
        print("Por favor, digite um número válido.")
    
    rand_num = random.randint(1, 100)
    print(f"Número aleatório entre 1 e 100: {rand_num}")

if __name__ == "__main__":
    main()
