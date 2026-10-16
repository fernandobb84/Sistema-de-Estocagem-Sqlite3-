from Db.classe import Banco_de_dados


class Estoque:
    def __init__(self, nome_produto, descricao, preco, quantidade, codigo, data):
        self.nome_produto = nome_produto
        self.descricao = descricao
        self.preco = float(preco)
        self.quantidade = int(quantidade)
        self.codigo_de_referencia = codigo
        self.data = data

    def salvar_produto(self, db=None):
        if db is None:
            db = Banco_de_dados()
        try:
            db.cursor.execute("""
                    INSERT INTO Armazenamento(Nome_produto, Descrição, Preco_unitario, Quantidade, Codigo_de_barra, Data_entrada) VALUES 
                                                (?,?,?,?,?,?)""",
                              (self.nome_produto, self.descricao, self.preco, self.quantidade, self.codigo_de_referencia, self.data),)

            db.salvar()
            print(
                f"O produto {self.nome_produto} foi adicionado(a) no estoque com sucesso!")

        except Exception as e:
            print(f"[ERRO]> O banco no pode ser acessado: {e}")

        finally:
            db.fechar()

    @staticmethod
    def listar_produtos(db=None):
        if db is None:
            db= Banco_de_dados()

        try:
            db.cursor.execute(" SELECT Nome_produto, Descrição, Preco_unitario, Quantidade, Codigo_de_barra, Data_entrada FROM Armazenamento")  
            produto_encotrado = db.cursor.fetchall()

            if not produto_encotrado:
                print("Nenhum produto encontrado")
                return
            
            print("[PRODUTOS NO ESTOQUE]")
            for produto in produto_encotrado:
                print(f"{"-"*50}\nNome: {produto[0]}\nDescrição: {produto[1]}\nPreço: {produto[2]}\nQuantidade: {produto[3]}\nCodigo de barras: {produto[4]}\nData de entrads: {produto[5]}\n{"-"*50}")
                
        except Exception as e:
            print(f"[ERRO]> O banco não pode ser acessado: {e}")
        finally:
            db.fechar()

    @staticmethod
    def calcular_quantidade(db=None):
        if db is None:
            db = Banco_de_dados()

        try:
            db.cursor.execute(" SELECT SUM(Quantidade) FROM Armazenamento")  
            quantidade_encontrada = db.cursor.fetchall()

            if not quantidade_encontrada:   
                print("Nenhuma quantidade encontrada!!")

            print('[QUANTIDADE DO ESTOQUE]')
        
            for total in quantidade_encontrada:
                print(f'A quantidade do estoque é: {total[0]}')

        except Exception as e:
            print(f"[ERRO]> O banco não pode ser acessado: {e}")
            
        finally:
            db.fechar()



# meu_estoque = Estoque()

# produto1 = Produto("Fones de ouvido", "10", "50", "1")
# produto2 = Produto("faca", "20", "20", "8")
# produto3 = Produto("caneta", "50", "1.50", "7")

# meu_estoque.adicionar_produto(produto1)
# meu_estoque.adicionar_produto(produto2)
# meu_estoque.adicionar_produto(produto3)

# meu_estoque.listar_produtos()

# total = meu_estoque.calcular_quantidade()
# print(f"Seu estoque tem {total} de itens cadastrados!!")
