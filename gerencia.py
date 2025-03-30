estoque = { #dicionário
    0:{'nome': 'maçã', 'quantidade': 1, 'valor':2.5},
    1:{'nome': 'banana', 'quantidade': 1, 'valor':2.5}
}

def listarItens():
    if not estoque: # caso estoque seja null, ele informará e irá retornar.
        print('Não há itens')
        return
    
    for chave, item in estoque.items(): #eu percorro os itens nos valores do dicionário de estoque e printo eles. #items me retorna uma tupla, ou seja, ela me retorna o ID e o valor referente ao ID, por isso preciso usar duas var para percorrer os itens do dic
        print(f"ID: {chave} | Nome: {item['nome']} | Quantidade: {item['quantidade']} | Valor: {item['valor']}")
    return

def adicionarItem():
    novo_id = max(estoque.keys(), default=-1) + 1 #a função Max pega o maior valor de uma estrutura de dados, dentro dela, eu uso o keys() pra pegar as chave do dicionário. Tendo o maior valor do dicionários, eu adiciono + 1 para fazer o novo id. Caso esteja vazio, começa em 0
    nome = input("Qual o nome do item: ").lower()
    quantidade = int(input(f"Quantidade de {nome} em estoque: "))
    valor = float(input(f"Valor de {nome}: "))
    estoque[novo_id] = { #adicionando o item ao dicionário
        'nome': nome,
        'quantidade': quantidade,
        'valor': valor
    }
    print("Item adicionado com sucesso!")
    print(estoque[novo_id])  # Mostra o item adicionado
    return

def removerItem():
    listarItens()
    chave = int(input("Digite a chave do item que deseja remover: "))

    if(chave not in estoque.keys()):
        print("Essa chave não existe no estoque")
        return
    
    del estoque[chave]
    print("Item removido com sucesso!")
    return

def editarItem():
    listarItens()
    chave = int(input("Que ID deseja editar: "))

    if(chave not in estoque.keys()):
        print("Essa ID não existe no estoque")
        return
    
    print(f"| ID 0:Nome - {estoque[chave]['nome']} | ID 1:Quantidade - {estoque[chave]['quantidade']} | ID 2:Valor - {estoque[chave]['valor']}")
    op = int(input("Qual ID deseja editar: "))

    if(op < 0 or op > 2):
        print("Esse ID não existe nas opções")
        return
    
    if(op == 0):
        nome = input("Digite o nome: ").lower()
        estoque[chave]['nome'] = nome
        
    elif(op == 1):
        quantidade = int(input("Digite a quantidade: "))
        estoque[chave]['quantidade'] = quantidade

    elif(op == 2):
        valor = float(input("Digite o valor: "))
        estoque[chave]['valor'] = valor

    print("Item alterado com sucesso!")
    
def buscaItem():
    if not estoque:
        print("O estoque está vazio.")
        return
    
    busca = input("O que está buscando: ").lower()
    encontrado = False  # Flag para verificar se algum item foi encontrado

    for chave, item in estoque.items():
        if busca == item['nome']:
            print(f"ID: {chave} | Nome: {item['nome']} | Quantidade: {item['quantidade']} | Valor: {item['valor']}")
            encontrado = True
    
    if not encontrado:
        print(f"Não há '{busca}' no estoque.")


def menu():
    while True:
        print("""
        1 - Listar itens
        2 - Adicionar item
        3 - Remover item
        4 - Editar item
        5 - Buscar item
        0 - Sair
        """)
        op = input("Sua opção: ")  
        if op == "1":
            listarItens()
            input("Aperte enter para voltar")

        elif op == "2":
            adicionarItem()
            input("Aperte enter para voltar")

        elif op == "3":
            removerItem()
            input("Aperte enter para voltar")

        elif op == "4":
            editarItem()
            input("Aperte enter para voltar")

        elif op == "5":
            buscaItem()
            input("Aperte enter para voltar")
            
        elif op == "0":
            print("Saindo...")
            break  # Encerra o loop corretamente
        else:
            print("Opção inválida! Tente novamente.")

menu()
