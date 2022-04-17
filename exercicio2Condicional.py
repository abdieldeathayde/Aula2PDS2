# perguntas = ["Esteve no local do crime? ", "Mora perto da vitima", "Devia para a vítima? ", "Já trabalho com a vítima?", "Telefonou para a vítima?"]
# respostas = []

pergunta1 = input('Esteve no local do crime? ')
pergunta2 = input('Mora perto da vítima? ')
pergunta3 = input('Devia para a vítima? ')
pergunta4 = input('Já trabalhou para a vítima? ')
pergunta5 = input('Telefonou para a vítima?')

cont = 0

if (pergunta1 == 'Sim' or pergunta1 == 'sim' or pergunta1 == "S" or pergunta1 == 's'):
    cont+=1   
elif (pergunta2 == 'Sim' or pergunta2 == 'sim' or pergunta2 == "S" or pergunta1 == 's'):
    cont += 1
elif (pergunta3 == 'Sim' or pergunta3 == 'sim' or pergunta3 == 'S' or pergunta3 == 's'):
    cont += 1
elif (pergunta4 == 'Sim' or pergunta4 == 'sim' or pergunta4 == 'S' or pergunta4 == 's'):
    cont += 1
elif (pergunta4 == 'Sim' or pergunta4 == 'sim' or pergunta4 == 'S' or pergunta4 == 's'):
    cont += 1
elif (pergunta5 == 'Sim' or pergunta5 == 'sim' or pergunta5 == 'S' or pergunta3 == 's'):
    cont +=1
else:
    print('Tente novamente')
    
if cont == 2:
    print('Suspeita')
elif cont >= 3 and cont<=4:
    print('Cumplice')
elif cont == 5:
    print('Assassino')