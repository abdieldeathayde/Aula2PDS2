telefones = {}
nomes = {}
cidades = []
contatos = {}

def agenda():
    opcao= input(" ---------MENU---------- \n ' 1 - Adicionar um contato(nome, telefone e cidade) na agenda; \n 2 - Remover contato por nome; \n 3 - Imprimir na tela os dados de uma das pessoas cadastradas (consulta por nome); \n 4 - Imprimir na tela a lista dos nomes que começam com uma letra indicada pelo usuário do sistema' ")
    if opcao == 1:
        cidade = input('Digite a Cidade do contato: ')
        cidades.append(cidade)
        telefone = int(input('Digite o número: '))
        nome = input('Digite o nome do contato: ')
        nomes.append(nome)
        contatos[nome] = telefone
        
        for contato in contatos:
            print(contatos[contato])
        
        
        
        #telefones.append(telefone)
        
        
        
    #remover um contato
    elif opcao == 2:
        posicao = int(input('Digite a posicao do contato'))
        del(nomes[posicao])
        del(telefones[posicao])
        del(cidades[posicao])
    elif opcao == 3:
        nomeBusca = input('Digite o nome que deseja buscar: ')
        