morangoKg = int(input('Digite a quantidade de Morango em Kg'))
macaKg = int(input('Digite a quantidade de maçã em Kg'))
valor_total = 0
while (morangoKg != 0 and macaKg != 0):
    if (morangoKg <= 5):
        precoMorango = 2.50
        valor_total += precoMorango
    elif (morangoKg > 5 and morangoKg < 8):
        precoMorango5Kg = 2.20
        valor_total += precoMorango
    elif (morangoKg >= 8):
        precoMorangoDesconto = precoMorango5Kg + (precoMorango5Kg * 0.10 )
        valor_total += precoMorangoDesconto
    if (macaKg <= 5):
        precoMaca = 1.80
        valor_total += precoMorango
    elif (macaKg > 5 and macaKg < 8):
        precoMaca5Kg = 1.50
        valor_total += precoMorango
    elif (macaKg >= 8):
        precoMacaDesconto = precoMaca5Kg + (precoMaca5Kg * 0.10 )
        valor_total += precoMacaDesconto