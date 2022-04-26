lista_medias = []
lista_meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

for i in range(12):
    temp = float(input('digite a temperatura'))
    lista_medias.append(temp)
    somatorio = 0
    somatorio += temp
    
temp_media = somatorio / 4

for i in range(12):
    temp_atual = lista_medias[i]
    mes_extenso = lista_meses[i]
    if temp_atual > temp_media:
        print("Temperatura : ", temp_atual)
        print("Mes:", mes_extenso)