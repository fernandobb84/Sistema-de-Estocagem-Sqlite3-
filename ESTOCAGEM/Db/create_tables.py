from classe import Banco_de_dados

db = Banco_de_dados()

db.cursor.execute("DROP TABLE Armazenamento ")

db.cursor.execute("""CREATE TABLE IF NOT EXISTS Clientes (
            Id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
            Nome_cliente VARCHAR(100) NOT NULL,
            CNPJ_CPF VARCHAR(50) NOT NULL UNIQUE,
            UF VARCHAR(2) NOT NULL,
            Rua TEXT NOT NULL,
            Cidade TEXT NOT NULL,
            Bairro TEXT NOT NULL,
            Numero INTEGER NOT NULL);
""")


db.cursor.execute("""CREATE TABLE IF NOT EXISTS Cargos (
            Id_cargo INTEGER PRIMARY KEY AUTOINCREMENT,
            Nome_cargo TEXT NOT NULL);
""")


db.cursor.execute("""CREATE TABLE IF NOT EXISTS Colaboradores (
            Id_colaborador  INTEGER PRIMARY KEY AUTOINCREMENT,
            Nome_colaborador VARCHAR(100) NOT NULL,
            CPF VARCHAR(15) NOT NULL,
            Data_Admissão DATETIME NOT NULL,
            Id_cargo INTEGER NOT NULL,
            FOREIGN KEY(id_cargo) REFERENCES Cargos(id_cargo));
""")


db.cursor.execute("""CREATE TABLE IF NOT EXISTS login (
            Id_login INTEGER PRIMARY KEY AUTOINCREMENT,
            Email VARCHAR(100) NOT NULL,
            Senha VARCHAR(50) NOT NULL,
            Id_cliente INTEGER,
            Id_colaborador INTEGER,
            FOREIGN KEY(id_cliente) REFERENCES Clientes(Id_cliente),
            FOREIGN KEY(id_colaborador) REFERENCES Colaboradores(id_colaborador ));
""")

db.cursor.execute("""CREATE TABLE IF NOT EXISTS Armazenamento (
                id_produto INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                Nome_produto TEXT NOT NULL,
                Descrição TEXT NOT NULL,
                Preco_unitario FLOAT NOT NULL CHECK (Preco_unitario > 0),
                Quantidade INT NOT NULL CHECK (Quantidade >= 0),
                Codigo_de_barra VARCHAR(50) NOT NULL UNIQUE,
                data_entrada DATETIME NOT NULL);
""")

db.cursor.execute('''CREATE TABLE IF NOT EXISTS Vendas (
                Id_vendas INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                data_vendas DATETIME NOT NULL,
                Valor_total DECIMAL NOT NULL,
                id_cliente INTEGER NOT NULL,
                id_colaborador INTEGER NOT NULL,
                FOREIGN KEY(id_cliente) REFERENCES Clientes(Id_cliente),
                FOREIGN KEY(id_colaborador) REFERENCES Colaboradores(id_colaborador ));
''')


db.cursor.execute('''CREATE TABLE IF NOT EXISTS Itens_vendas (
                id_item INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                id_vendas INTEGER NOT NULL,
                id_produto INTEGER NOT NULL,
                quantidade_vendida INTEGER NOT NULL,
                preço_praticado INTEGER NOT NULL,
                FOREIGN KEY(id_vendas) REFERENCES Vendas(Id_vendas),
                FOREIGN KEY(id_produto) REFERENCES Armazenamento(id_produto));
''')


db.conexao.commit()
db.conexao.close()
