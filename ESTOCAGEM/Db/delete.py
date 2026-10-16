import classe 

db = classe.Banco_de_dados()

db.cursor.execute("DELETE FROM Cargos")
db.cursor.execute("DELETE FROM sqlite_sequence WHERE name = 'Cargos';")

db.salvar()
print("Sucesso!!")
db.fechar()
