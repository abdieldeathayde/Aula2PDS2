candidato1 = input('Digite seu nome: ')
candidato2 = input('Digite o seu nome: ')
candidato3 = input('Por favor, digite seu nome: ')

numeroEleitores = int(input('Digite a quantidade de eleitores: '))
cand1 = 0
cand2 = 0
cand3 = 0
for i in range (numeroEleitores):
    voto = int(input(f'Digite \n 1 - {candidato1} \n 2 - {candidato2} \n 3 - {candidato3} \n '))
    if voto == 1:
        cand1 += 1
    elif voto  == 2:
        cand2 += 1
    elif voto == 3:
        cand3 += 1
    else:
        print('Opção inválida')
        print(f'Digite \n 1 - {candidato1} \n 2 - {candidato2} \n 3 - {candidato3} \n')
print(f' O candidato {candidato1} teve {cand1} Votos \n O candidato {candidato2} teve {cand2} votos \n O candidato {candidato3} teve {cand3} votos ')