
alunos_notas = ('Ana', 8.5, 'Carlos', 7.0, 'Beatriz', 9.2, 'Daniel', 6.8, 'Eduarda', 8.0)


print("Nomes dos alunos:")
for i in range(0, len(alunos_notas), 2):
    print(alunos_notas[i])


print("\nNotas dos alunos:")
for i in range(1, len(alunos_notas), 2): 
    print(alunos_notas[i])
