import sqlite3

connection = sqlite3.connect("caixa.db")

cursor = connection.cursor()
query = 'update lancamento set transaction_status = ? where id = ?'
values = ('alterado','1')

cursor.execute(query,values)

connection.commit()
connection.close()