import sqlite3

conn = sqlite3.connect('supremerent.db')
cursor = conn.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='about_servici';")
table_exists = cursor.fetchone()

if table_exists:
    print("Tabela 'about_servici' există.")
    cursor.execute("PRAGMA table_info(about_servici);")
    columns = cursor.fetchall()
    print("Structura tabelei:")
    for column in columns:
        print(column)
else:
    print("Tabela 'about_servici' nu există.")

conn.close()
