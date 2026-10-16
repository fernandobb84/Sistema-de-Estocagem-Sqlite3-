from datetime import datetime
from Db.classe import Banco_de_dados
from pathlib import Path

def buscar_cargos():
    db = Banco_de_dados()
    try:
        db.cursor.execute("SELECT Id_cargo, Nome_cargo FROM Cargos")

        print(f'Cargos registrado.\n {"="*35}')
        for linhas in db.cursor.fetchall():
            print(f"ID: {linhas[0]} | CARGO: {linhas[1]}")
            print(f"{"="*35}\n")
            db.salvar()
    except Exception as e:
        print(f"[ERRO]> O banco não pode ser acessado: {e}")
        registrar_logs("erro", f"Erro de conexão com o banco: {e}")
    finally:
        db.fechar()


def nome():
    return input("Digite o nome: ").capitalize().strip()


def verificar_email():
    while True:
        email = input("Digite o email: ").strip()
        if "@" in email and "." in email:
            return email
        print("Email inválido. Por favor, insira um email válido.")
        registrar_logs('erro', "formato de email invalido.")


def verificar_senha():
    while True:
        senha = input("Digite a senha: ").strip()
        if len(senha) >= 8:
            return senha
        print("A senha deve conter pelo menos 8 caracteres. Tente novamente.")
        registrar_logs("erro", "Formato de senha invalido")


def verificar_login(Email, Senha, db=None):

    if db is None:
        db = Banco_de_dados()

    try:
        query = """
            SELECT c.Nome_cargo
            FROM login l
            JOIN Colaboradores col ON l.Id_colaborador = col.Id_colaborador
            JOIN Cargos c ON col.Id_cargo = c.Id_cargo
            WHERE l.Email = ? AND l.Senha = ?
        """

        db.cursor.execute(query, (Email, Senha),)

        usuario = db.cursor.fetchone()

        if usuario:
            db.salvar()
            cargo = usuario[0]
            print(f"Cargo encontrado: {cargo}")
            return cargo

        print("Email ou senha incorretos ou usuario não e colaborador.")
        registrar_logs("erro", "Email ou senha incorretos.")
        return None

    except Exception as e:
        print(f"Erro: O banco não pode ser acessado -> {e} ")
        registrar_logs("erro", f"Erro de conexão com o banco: {e}")
        return None
    finally:
        db.fechar()


def registrar_logs(tipo, mensagem):
    
    pasta_login = Path("Logs_save")
    pasta_login.mkdir(parents=True, exist_ok=True)

    arquivo_login = pasta_login / "sistema_login.txt"    
    
    try:
        data_atual = datetime.now().strftime("%d/%m/%Y|%HH:%MM")

        with open(arquivo_login, "a", encoding="utf-8") as arquivo:
            arquivo.write(f"[{tipo.upper()}]> [{mensagem.capitalize()}] -> [{data_atual}]\n")
    except Exception as e:
        print(f"[ERRO]> erro: {e}")