numerosAlunos = []
alturasCentimetros = [] 
menor = 200
maior = 0
for i in range(3):
    numeroAluno = int(input('Digite seu numero de aluno'))
    numerosAlunos.append(numeroAluno)
    alturaCentimetros = int(input('Digite sua altura em centimetros'))
    alturasCentimetros.append(alturaCentimetros)
    
    if (alturasCentimetros[i] < menor):
        menor = alturasCentimetros[i]
        numeroAlunoAtualMenor = numerosAlunos[i]
        #print(f'o aluno numero {numeroAlunoAtualMenor} é o menor e tem {menor} centímetros')
        
    if (alturasCentimetros[i] > maior):
        maior = alturasCentimetros[i]
        numeroAlunoAtualMaior = numerosAlunos[i]
        #print(f'O aluno numero {numeroAlunoAtualMaior} é o maior e tem {maior} centimetros')

print(f'O aluno numero {numeroAlunoAtualMenor} é o menor e tem {menor} centimetros')
print(f'O aluno numero {numeroAlunoAtualMaior} é o maior e tem {maior} centimetros')