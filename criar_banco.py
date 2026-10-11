import sqlite3  # o SQLite já vem embutido no Python — nada pra instalar

# 1) Conecta ao banco. Se o arquivo "caixa.db" não existir, o SQLite CRIA ele aqui.
conexao = sqlite3.connect("caixa.db")

# 2) O cursor é quem executa os comandos dentro do banco.
cursor = conexao.cursor()

# 3) Cria a tabela. "IF NOT EXISTS" = só cria se ainda não existir
#    (assim você pode rodar de novo sem dar erro).
cursor.execute("""
CREATE TABLE IF NOT EXISTS lancamento (
    id                 INTEGER PRIMARY KEY,
    restaurante_id     INTEGER NOT NULL DEFAULT 1,
    transaction_type   TEXT    NOT NULL CHECK (transaction_type IN ('entrada','saida')),
    description        TEXT,
    gross_value        INTEGER NOT NULL,
    tax_discount       INTEGER NOT NULL DEFAULT 0,
    natureza           TEXT    NOT NULL CHECK (natureza IN ('negocio','pessoal')),
    financial_account  TEXT,
    category           TEXT,
    channel            TEXT,
    payment_method     TEXT,
    transaction_status TEXT    NOT NULL,
    transaction_date   TEXT    NOT NULL,
    settlement_date    TEXT,
    data_vencimento    TEXT,
    comentary          TEXT,
    created_at         TEXT    NOT NULL DEFAULT (datetime('now'))
)
""")

# 4) commit = salva de verdade a mudança no arquivo do banco.
conexao.commit()

# 5) Confirmação: pergunta ao próprio banco quais tabelas existem agora.
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
print("Tabelas no banco:", cursor.fetchall())

# 6) Fecha a conexão (boa prática: sempre fechar quando terminar).
conexao.close()
print("Pronto! Banco 'caixa.db' criado com a tabela 'lancamento'.")