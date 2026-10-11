import sqlite3

connect = sqlite3.connect("caixa.db")

cursor = connect.cursor()

query = (
    """
    insert into lancamento (
        restaurante_id,
        transaction_type,
        description,
        gross_value,
        tax_discount,
        natureza,
        transaction_status,
        transaction_date) 
        values (?,?,?,?,?,?,?,?)
    """
)

values = (
        1,
        'entrada',
        'frango tradicional',
        9000,
        2600,
        'negocio',
        'realizada',
        '2026-10-11'
    )

cursor.execute(query,values)
connect.commit()

connect.close()