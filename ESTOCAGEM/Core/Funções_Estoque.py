def nome_produto():
    nome_do_item = input("Digite o nome do produto: ").capitalize().strip()
    return nome_do_item

def adicionar_quantidade():
    registrar_quantidade = int(input("Digite a quantidade: "))
    return registrar_quantidade

def adicionar_preco():
    registrar_preco = float(input("Digite o preço por unidade: "))
    return registrar_preco

def descricao():
    descricao = input("Digite uma descrição breve do produto\n ").capitalize().strip()
    return descricao