from datetime import datetime

import classe

db = classe.Banco_de_dados()

data = datetime.now().strftime("%d/%m/%Y")

db.cursor.execute("UPDATE Colaboradores SET Data_Admissão = ? WHERE Id_colaborador = 3", (data,))
db.salvar()
print("SUCESSO")
db.fechar()