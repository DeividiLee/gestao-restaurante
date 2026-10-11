import sqlite3

connect = sqlite3.connect("caixa.db")

cursor = connect.cursor()
query = "delete from lancamento where id = ?"
value = (1,)

cursor.execute(query,value)
connect.commit()

connect.close()