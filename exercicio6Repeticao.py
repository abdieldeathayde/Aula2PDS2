n = 1
n1 = 0 
n2 = 0
n3 = 0
n4 = 0

while (n >= 0):
    n = int(input('Digite o numero:'))
    if (n >= 0 and n <= 25):
        n1 += 1
    elif (n >= 26 and n <= 50):
        n2 += 1
    elif (n >= 51 and n <= 75):
        n3 += 1
    elif (n >= 76 and n <= 100):
        n4 += 1
    else:
        print('opcao invalida')
        
print(f'A quantidade de numeros entre 0 e 25 é {n1} \n  A quantidade de numeros entre 26 a 50 é {n2} \n A quantidade de numeros entre 51 e 75 é {n3} \n A quantidade de numeros entre 76 e 100 é {n4}')
        