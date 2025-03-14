# Exercício 1: Par ou Ímpar?
class ParImpar:
    def __init__(self, numero):
        self.numero = numero

    def verificar(self):
        if self.numero % 2 == 0:
            return "Par"
        else:
            return "Ímpar"


# Exercício 2: Maior Número
class MaiorNumero:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def obter_maior(self):
        if self.num1 == self.num2:
            return "Os números são iguais."
        else:
            return max(self.num1, self.num2)


# Exercício 3: Classificação de Idade
class ClassificacaoIdade:
    def __init__(self, idade):
        self.idade = idade

    def classificar(self):
        if self.idade < 18:
            return "Menor de idade"
        elif self.idade < 60:
            return "Adulto"
        else:
            return "Idoso"


# Exercício 4: Cálculo de Média e Aprovação
class MediaAprovacao:
    def __init__(self, nota1, nota2):
        self.nota1 = nota1
        self.nota2 = nota2

    def calcular_media(self):
        return (self.nota1 + self.nota2) / 2

    def avaliar(self):
        media = self.calcular_media()
        if media >= 7:
            return f"Média: {media:.2f} - Aprovado"
        elif media >= 5:
            return f"Média: {media:.2f} - Recuperação"
        else:
            return f"Média: {media:.2f} - Reprovado"


# Exercício 5: Verificação de Triângulo
class VerificacaoTriangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def eh_triangulo(self):
        # A soma de dois lados deve ser maior que o terceiro lado
        return (self.lado1 + self.lado2 > self.lado3) and \
               (self.lado1 + self.lado3 > self.lado2) and \
               (self.lado2 + self.lado3 > self.lado1)

    def verificar(self):
        if self.eh_triangulo():
            return "Os lados formam um triângulo válido."
        else:
            return "Os lados não formam um triângulo válido."


def main():
    # Exercício 1: Par ou Ímpar?
    print("Exercício 1: Par ou Ímpar?")
    try:
        numero = int(input("Digite um número inteiro: "))
    except ValueError:
        print("Valor inválido!")
    else:
        par_impar = ParImpar(numero)
        print(f"O número {numero} é {par_impar.verificar()}.")

    # Exercício 2: Maior Número
    print("\nExercício 2: Maior Número")
    try:
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
    except ValueError:
        print("Valor inválido!")
    else:
        maior = MaiorNumero(num1, num2)
        resultado = maior.obter_maior()
        print("Resultado:", resultado)

    # Exercício 3: Classificação de Idade
    print("\nExercício 3: Classificação de Idade")
    try:
        idade = int(input("Digite sua idade: "))
    except ValueError:
        print("Valor inválido!")
    else:
        classificacao = ClassificacaoIdade(idade)
        print("Classificação:", classificacao.classificar())

    # Exercício 4: Cálculo de Média e Aprovação
    print("\nExercício 4: Cálculo de Média e Aprovação")
    try:
        nota1 = float(input("Digite a primeira nota: "))
        nota2 = float(input("Digite a segunda nota: "))
    except ValueError:
        print("Valor inválido!")
    else:
        media_aluno = MediaAprovacao(nota1, nota2)
        print(media_aluno.avaliar())

    # Exercício 5: Verificação de Triângulo
    print("\nExercício 5: Verificação de Triângulo")
    try:
        lado1 = float(input("Digite o primeiro lado do triângulo: "))
        lado2 = float(input("Digite o segundo lado do triângulo: "))
        lado3 = float(input("Digite o terceiro lado do triângulo: "))
    except ValueError:
        print("Valor inválido!")
    else:
        triangulo = VerificacaoTriangulo(lado1, lado2, lado3)
        print(triangulo.verificar())


if __name__ == "__main__":
    main()
