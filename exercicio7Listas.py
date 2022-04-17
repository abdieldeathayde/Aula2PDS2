n = 1
notas = []
soma = 0
while (n >= 0):
    n = int(input('Digite a nota'))
    if (n >= 0):
        notas.append(n)
print(notas)
notas.reverse()
print(notas)

for i in range (len(notas)):
    soma += notas[i]
    media = soma / len(notas)
    if notas[i] > media:
        notaAtual = notas[i]
        print(f'nota(s) {notaAtual} são maiores que a media' )
    elif (notas[i] < 7):
        notaAtual2 = notas[i]
        print(f'As notas {notaAtual2} são menores que 7')
    else:
        print('Valor incorreto')
print(soma)
print(media)