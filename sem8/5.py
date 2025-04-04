class SaldoInsuficienteError(Exception):
    """Exceção personalizada para saldo insuficiente."""
    pass

def realizar_saque(saldo, valor):
    if valor > saldo:
        raise SaldoInsuficienteError("Saldo insuficiente para realizar o saque.")
    return saldo - valor

def main():
    saldo = 1000.00
    print(f"Saldo atual: R$ {saldo:.2f}")
    try:
        valor_saque = float(input("Digite o valor para saque: R$ "))
        novo_saldo = realizar_saque(saldo, valor_saque)
    except ValueError:
        print("Erro: Entrada inválida. Por favor, digite um número.")
    except SaldoInsuficienteError as e:
        print("Erro:", e)
    else:
        print(f"Saque realizado com sucesso. Novo saldo: R$ {novo_saldo:.2f}")

if __name__ == "__main__":
    main()
