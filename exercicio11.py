total_gasto = 0
def imprimeOpcoes():
    opcao = 4
    
    while opcao != 0:
        total_gasto = 0
        opcao = int(input("-----------------------MENU----------------------- \n Escolha uma opcao \n 0 - Sair \n 1 - A vista com 10'%'  de desconto \n 2 - Em duas vezes(Preço da etiqueta) \n 3 - De 3 até 10 vezes com 3'%' de juros ao mês(Apenas para comprar acima de R$ 100,00)"))
        #print(f'Opcao Escolhida: {opcao}')
        return opcao

def AVista():
    total_gasto = float(input('Por favor, digite o total gasto na Preçolandia!'))
    total_gasto = total_gasto - (total_gasto * 0.10)
    print(f'o total gasto é: {total_gasto}')

def duasVezes():
    total_gasto = float(input('Por favor, digite o total gasto na Preçolandia!'))
    total_gasto = total_gasto
    print(f'o total gasto é: {total_gasto}')

def De3A10Vezes():
    total_gasto = float(input('Por favor, digite o total gasto na Preçolandia!'))
    if total_gasto > 100.0:
        total_gasto = total_gasto + (total_gasto * 0.3)
        print(f'o total gasto é: {total_gasto}')
        
    else: 
        print('Essa opção só é valida para compras acima de R$ 100,00!')
def main():
    
    imprimeOp =  imprimeOpcoes()
    
    if imprimeOp == 0:
        exit()
    elif imprimeOp == 1:
        AVista()
    elif imprimeOp == 2:
        duasVezes()
    elif imprimeOp == 3:
        De3A10Vezes()
    else:
        print('Opção inválida, tente novamente!')

main()

