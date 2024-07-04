import sqlite3

# Connessione al database (crea il file se non esiste)
conn = sqlite3.connect('users.db')

# Creazione del cursore
cursor = conn.cursor()

# Creazione della tabella users
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    email TEXT PRIMARY KEY,
    last_login DATETIME,
    login_count INTEGER
)
''')

# Commit delle modifiche e chiusura della connessione
conn.commit()
conn.close()

print("Database e tabella creati con successo.")
