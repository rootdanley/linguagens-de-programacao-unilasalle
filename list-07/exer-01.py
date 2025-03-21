
alunos = {}


while len(alunos) < 3:
    nome = input("Digite o nome do aluno: ")
    try:
        nota = float(input(f"Digite a nota do aluno {nome}: "))
        alunos[nome] = nota 
    except ValueError:
        print("Nota inválida. Por favor, insira um valor numérico válido.")


print("\nLista de alunos e suas notas:")
for nome, nota in alunos.items():
    print(f"{nome}: {nota:.1f}")
