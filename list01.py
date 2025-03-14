import math

# 1. Cálculo da Área do Círculo
class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        return math.pi * (self.raio ** 2)


# 2. Conversão de Temperatura (Celsius para Fahrenheit)
class ConversorTemperatura:
    def __init__(self, celsius):
        self.celsius = celsius

    def celsius_para_fahrenheit(self):
        return (self.celsius * 9/5) + 32


# 3. Média de Três Números
class MediaTresNumeros:
    def __init__(self, n1, n2, n3):
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3

    def calcular_media(self):
        return (self.n1 + self.n2 + self.n3) / 3


# 4. Cálculo do Salário Mensal
class SalarioMensal:
    def __init__(self, horas_trabalhadas, valor_hora):
        self.horas_trabalhadas = horas_trabalhadas
        self.valor_hora = valor_hora

    def calcular_salario(self):
        return self.horas_trabalhadas * self.valor_hora


# 5. Conversão de Medidas – Metros para Centímetros
class ConversorMedidas:
    def __init__(self, metros):
        self.metros = metros

    def metros_para_centimetros(self):
        return self.metros * 100


def main():
    # 1. Cálculo da Área do Círculo
    print("1. Cálculo da Área do Círculo")
    try:
        raio = float(input("Digite o valor do raio do círculo: "))
        circulo = Circulo(raio)
        area = circulo.calcular_area()
        print(f"A área do círculo é: {area:.2f}")
    except ValueError:
        print("Valor inválido para o raio.")

    print("-" * 40)

    # 2. Conversão de Temperatura (Celsius -> Fahrenheit)
    print("2. Conversão de Temperatura (Celsius -> Fahrenheit)")
    try:
        celsius = float(input("Digite a temperatura em graus Celsius: "))
        conversor = ConversorTemperatura(celsius)
        fahrenheit = conversor.celsius_para_fahrenheit()
        print(f"{celsius} °C equivalem a {fahrenheit:.2f} °F.")
    except ValueError:
        print("Valor inválido para a temperatura.")

    print("-" * 40)

    # 3. Média de Três Números
    print("3. Média de Três Números")
    try:
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
        n3 = float(input("Digite o terceiro número: "))
        media_obj = MediaTresNumeros(n1, n2, n3)
        media = media_obj.calcular_media()
        print(f"A média dos três números é: {media:.2f}")
    except ValueError:
        print("Valor inválido. Certifique-se de digitar números.")

    print("-" * 40)

    # 4. Cálculo do Salário Mensal
    print("4. Cálculo do Salário Mensal")
    try:
        horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))
        valor_hora = float(input("Digite o valor recebido por hora: "))
        salario_obj = SalarioMensal(horas_trabalhadas, valor_hora)
        salario = salario_obj.calcular_salario()
        print(f"O salário mensal é: R$ {salario:.2f}")
    except ValueError:
        print("Valor inválido. Digite números para horas e valor por hora.")

    print("-" * 40)

    # 5. Conversão de Medidas – Metros para Centímetros
    print("5. Conversão de Medidas – Metros para Centímetros")
    try:
        metros = float(input("Digite o valor em metros: "))
        conversor_medidas = ConversorMedidas(metros)
        centimetros = conversor_medidas.metros_para_centimetros()
        print(f"{metros} metro(s) equivalem a {centimetros:.2f} centímetro(s).")
    except ValueError:
        print("Valor inválido. Digite um número válido para metros.")

    print("-" * 40)


if __name__ == "__main__":
    main()
