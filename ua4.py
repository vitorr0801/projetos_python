nome_aluno = input('Digite o nome do aluno:')
notas = []
ct = 0
soma = 0
while True:
    nota = input('Digite uma nota(ou fim para encerrar):')
    if nota.lower() == 'fim':
        break
    notas.append(float(nota))
    ct += 1
    soma += float(nota)
media = soma/ct
print('Nome do aluno:', nome_aluno)
print('Média:', media)

