dicio = {
  input("Nome do aluno 1: "): float(input("Nota do aluno 1: ")),
  input("\nNome do aluno 2: "): float(input("Nota do aluno 2: ")),
  input("\nNome do aluno 3: "): float(input("Nota do aluno 3: ")),
  input("\nNome do aluno 4: "): float(input("Nota do aluno 4: ")),
  input("\nNome do aluno 5: "): float(input("Nota do aluno 5: "))
}

i = 0
melhores_alunos = []
for nome, nota in dicio.items():  
    if nota == max(dicio.values()):
        melhores_alunos = melhores_alunos + [nome]

print(melhores_alunos," com nota: {0:.2f}".format(max(dicio.values())))
    
