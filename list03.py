# Exercício 1: Contagem Progressiva
class ContagemProgressiva:
    def __init__(self, numero):
        self.numero = numero

    def exibir_contagem(self):
        # Retorna uma lista com os números de 1 até o número informado
        return list(range(1, self.numero + 1))


# Exercício 2: Soma de Números Positivos
class SomaNumerosPositivos:
    def __init__(self):
        self.soma = 0

    def somar(self):
        # Solicita números repetidamente até que um número negativo seja digitado.
        # Soma somente os números positivos.
        while True:
            try:
                num = int(input("Digite um número (número negativo para encerrar): "))
            except ValueError:
                print("Valor inválido. Tente novamente.")
                continue

            if num < 0:
                break
            self.soma += num
        return self.soma


# Exercício 3: Tabuada de um Número
class TabuadaNumero:
    def __init__(self, numero):
        self.numero = numero

    def exibir_tabuada(self):
        # Gera a tabuada do número (de 1 a 10) em formato de lista de strings
        resultado = []
        for i in range(1, 11):
            resultado.append(f"{self.numero} x {i} = {self.numero * i}")
        return resultado


# Exercício 4: Números Ímpares em um Intervalo
class NumerosImparesIntervalo:
    def __init__(self, inicio, fim):
        self.inicio = inicio
        self.fim = fim

    def obter_impares(self):
        # Caso os números estejam fora de ordem, ajusta o intervalo
        inicio = min(self.inicio, self.fim)
        fim = max(self.inicio, self.fim)
        # Retorna os números ímpares entre inicio e fim (inclusive)
        return [num for num in range(inicio, fim + 1) if num % 2 != 0]


# Exercício 5: Sequência de Fibonacci
class Fibonacci:
    def __init__(self, n):
        self.n = n

    def gerar_fibonacci(self):
        # Gera os N primeiros termos da sequência de Fibonacci
        if self.n <= 0:
            return []
        elif self.n == 1:
            return [0]
        fibonacci_seq = [0, 1]
        while len(fibonacci_seq) < self.n:
            proximo = fibonacci_seq[-1] + fibonacci_seq[-2]
            fibonacci_seq.append(proximo)
        return fibonacci_seq


# Função principal para demonstrar o funcionamento de cada exercício
def main():
    # Exercício 1: Contagem Progressiva
    print("Exercício 1: Contagem Progressiva")
    try:
        numero = int(input("Digite um número inteiro positivo: "))
    except ValueError:
        print("Valor inválido!")
        return

    if numero <= 0:
        print("O número deve ser positivo!")
    else:
        cp = ContagemProgressiva(numero)
        contagem = cp.exibir_contagem()
        for num in contagem:
            print(num)

    # Exercício 2: Soma de Números Positivos
    print("\nExercício 2: Soma de Números Positivos")
    soma_obj = SomaNumerosPositivos()
    soma = soma_obj.somar()
    print("Soma dos números positivos digitados:", soma)

    # Exercício 3: Tabuada de um Número
    print("\nExercício 3: Tabuada de um Número")
    try:
        num_tabuada = int(input("Digite um número inteiro para exibir sua tabuada: "))
    except ValueError:
        print("Valor inválido!")
        return

    tabuada = TabuadaNumero(num_tabuada)
    for linha in tabuada.exibir_tabuada():
        print(linha)

    # Exercício 4: Números Ímpares em um Intervalo
    print("\nExercício 4: Números Ímpares em um Intervalo")
    try:
        inicio = int(input("Digite o primeiro número do intervalo: "))
        fim = int(input("Digite o segundo número do intervalo: "))
    except ValueError:
        print("Valor inválido!")
        return

    impares_obj = NumerosImparesIntervalo(inicio, fim)
    impares = impares_obj.obter_impares()
    print("Números ímpares no intervalo:", impares)

    # Exercício 5: Sequência de Fibonacci
    print("\nExercício 5: Sequência de Fibonacci")
    try:
        n_fib = int(input("Digite o número de termos da sequência de Fibonacci que deseja ver: "))
    except ValueError:
        print("Valor inválido!")
        return

    fib_obj = Fibonacci(n_fib)
    fibonacci_seq = fib_obj.gerar_fibonacci()
    print("Sequência de Fibonacci:", fibonacci_seq)


if __name__ == "__main__":
    main()
