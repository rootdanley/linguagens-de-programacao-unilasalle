# Exercício 1: Soma dos Elementos de uma Lista
class ListaSoma:
    def __init__(self, lista):
        self.lista = lista

    def calcular_soma(self):
        return sum(self.lista)


# Exercício 2: Encontrar o Maior e o Menor Número
class ListaMaiorMenor:
    def __init__(self, lista):
        self.lista = lista

    def obter_maior(self):
        return max(self.lista)

    def obter_menor(self):
        return min(self.lista)


# Exercício 3: Remover Duplicatas
class ListaSemDuplicatas:
    def __init__(self, lista):
        self.lista = lista

    def remover_duplicatas(self):
        nova_lista = []
        for num in self.lista:
            if num not in nova_lista:
                nova_lista.append(num)
        return nova_lista


# Exercício 4: Inverter a Lista
class ListaInvertida:
    def __init__(self, lista):
        self.lista = lista

    def inverter(self):
        # Usando slicing para inverter a lista
        return self.lista[::-1]


# Exercício 5: Contar Ocorrências de um Elemento
class ContadorOcorrencias:
    def __init__(self, lista):
        self.lista = lista

    def contar(self, elemento):
        return self.lista.count(elemento)


# Função principal para demonstrar os exercícios
def main():
    # Exercício 1: Soma dos Elementos de uma Lista
    print("Exercício 1: Soma dos Elementos de uma Lista")
    entrada = input("Digite uma lista de números inteiros separados por espaço: ")
    lista_numeros = list(map(int, entrada.split()))
    soma_obj = ListaSoma(lista_numeros)
    soma = soma_obj.calcular_soma()
    print("Soma dos elementos:", soma)

    # Exercício 2: Encontrar o Maior e o Menor Número
    print("\nExercício 2: Encontrar o Maior e o Menor Número")
    entrada = input("Digite uma lista de números separados por espaço: ")
    lista_numeros = list(map(int, entrada.split()))
    mm_obj = ListaMaiorMenor(lista_numeros)
    maior = mm_obj.obter_maior()
    menor = mm_obj.obter_menor()
    print("Maior número:", maior)
    print("Menor número:", menor)

    # Exercício 3: Remover Duplicatas
    print("\nExercício 3: Remover Duplicatas")
    entrada = input("Digite uma lista de números separados por espaço: ")
    lista_numeros = list(map(int, entrada.split()))
    rd_obj = ListaSemDuplicatas(lista_numeros)
    lista_sem_duplicatas = rd_obj.remover_duplicatas()
    print("Lista sem duplicatas:", lista_sem_duplicatas)

    # Exercício 4: Inverter a Lista
    print("\nExercício 4: Inverter a Lista")
    entrada = input("Digite uma lista de palavras separadas por espaço: ")
    lista_palavras = entrada.split()
    inv_obj = ListaInvertida(lista_palavras)
    lista_invertida = inv_obj.inverter()
    print("Lista invertida:", lista_invertida)

    # Exercício 5: Contar Ocorrências de um Elemento
    print("\nExercício 5: Contar Ocorrências de um Elemento")
    entrada = input("Digite uma lista de números separados por espaço: ")
    lista_numeros = list(map(int, entrada.split()))
    num = int(input("Digite o número que deseja contar: "))
    cont_obj = ContadorOcorrencias(lista_numeros)
    ocorrencias = cont_obj.contar(num)
    print(f"O número {num} aparece {ocorrencias} vezes na lista.")


if __name__ == "__main__":
    main()
