def mediaAlunos (nota1, nota2, nota3, tipoMedia):
    peso1 = 5
    peso2 = 3
    peso3 = 2 
    if tipoMedia == 'A':
        print ((nota1+nota2+nota3) / 3)
    elif tipoMedia == 'P':
        print((nota1 * peso1 ) + (nota2 * peso2) + (nota3 * peso3) / (peso1 + peso2 + peso3))
    else:
        print(0) 
mediaAlunos(5,7,4, 'A')