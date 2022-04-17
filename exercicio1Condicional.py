idade = int(input('Digite a sua idade: '))

if (idade < 16):
    print('proibida')
    
elif (idade >= 16 and idade < 18 or idade >= 65):
    print('optativa')

elif (idade >= 18 and idade < 65):
    print('obrigatória')