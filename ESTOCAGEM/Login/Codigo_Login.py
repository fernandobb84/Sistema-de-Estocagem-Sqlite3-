from Db.classe import Banco_de_dados

class Cadastro:
    def __init__(self, cliente,documento, uf, rua, cidade, bairro, numero, email, senha):
        self.cliente = cliente
        self.documento = documento
        self.uf = uf
        self.rua = rua
        self.cidade = cidade
        self.bairro = bairro
        self.numero = numero
        self.email = email
        self.senha = senha
        
        
    def salvar_dados(self, db=None):

        if db is None:
            db = Banco_de_dados()
            
        try:
            db.cursor.execute(''' INSERT INTO Clientes(Nome_cliente,CNPJ_CPF, UF, Rua, Cidade, Bairro, Numero) VALUES
                                (?,?,?,?,?,?,?)''', 
                                (self.cliente, self.documento, self.uf, self.rua, self.cidade, self.bairro, self.numero ),)
            
            id_gerado_cliente = db.cursor.lastrowid

            db.cursor.execute('''INSERT INTO login(Email, Senha, Id_cliente) VALUES
                                    (?,?,?)''', (self.email, self.senha, id_gerado_cliente),)

            db.salvar()
            print(f"\n[CLIENTE]->{self.cliente} foi cadastrado com sucesso!!")

        except Exception as e:
            print(f"[ERRO]> O banco não pode ser acessado -> {e}")
        finally:
            db.fechar()
    
class Cargo:
    def __init__(self, nome_cargo):
        self.nome_cargo = nome_cargo
        
    def criar_cargo(self, db=None):
        if db is None:
             db = Banco_de_dados()

        try:
            print("Adicione um cargo\n")
            db.cursor.execute(""" INSERT INTO Cargos(Nome_cargo) VALUES
                                (?)""", (self.nome_cargo,))
            
            db.salvar()
            print(f"O cargo {self.nome_cargo} foi criado com sucesso!")
        except Exception as e:
                print(f"[ERRO]> O banco no pode ser acessado -> {e}")
        
        finally:
            db.fechar()

class Colaborador:
    def __init__(self, nome, documento, data_admissao, seu_cargo, email, senha):
        self.nome = nome
        self.documento = documento
        self.data_admissao = data_admissao
        self.seu_cargo = seu_cargo
        self.email = email
        self.senha = senha 

    def adicionar_colaborador(self, db=None):
        if db is None:
            db = Banco_de_dados()
        try:
            db.cursor.execute("""INSERT INTO Colaboradores(Nome_colaborador, CPF, Data_admissão, Id_cargo) VALUES
                                                        (?,?,?,?)""", (self.nome, self.documento, self.data_admissao, self.seu_cargo),)
            
            id_gerado_colaborador = db.cursor.lastrowid

            db.cursor.execute('''INSERT INTO login(Email, Senha, Id_cliente, Id_colaborador) VALUES 
                                                    (?,?, NULL, ?)''', (self.email, self.senha, id_gerado_colaborador),)
            
            db.salvar()
            if self.seu_cargo == 1:
                self.seu_cargo = "Administrador"
            elif self.seu_cargo == 2:
                self.seu_cargo = "Estoquista"
            else:
                self.seu_cargo = "Caixa"

            print(f"O Colaborador [{self.nome}] e seu cargo [{self.seu_cargo}] foram adicionados com sucesso !!")
        except Exception as e:
            print(f"[ERRO]> O banco não pode ser acessado: {e}")
        finally:
            db.fechar()