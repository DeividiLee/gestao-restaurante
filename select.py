import sqlite3

connect = sqlite3.connect("caixa.db")

cursor = connect.cursor()

cursor.execute(
    'select * from lancamento'
)
print('insert do lancamento:', cursor.fetchall())

connect.close()