import sqlite3


def get_all_servicii():
    conn = sqlite3.connect('supremerent.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM about_servici')
    serviciu = cursor.fetchall()
    conn.close()
    return serviciu

def add_serviciu(serviciu):
    conn = sqlite3.connect('supremerent.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO about_servici (serviciu) VALUES (?)', (serviciu,))
    conn.commit()
    conn.close()