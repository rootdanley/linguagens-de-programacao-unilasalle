def main():
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = num1 / num2
    except ZeroDivisionError:
        print("Erro: Divisão por zero não é permitida.")
    except ValueError:
        print("Erro: Por favor, digite números válidos.")
    else:
        print(f"O resultado de {num1} / {num2} é {resultado}")

if __name__ == "__main__":
    main()
