import sqlite3

# Conexión a la base de datos (se crea si no existe)
conn = sqlite3.connect('Facultad.db')
cursor = conn.cursor()

# Creación de la tabla
cursor.execute('''CREATE TABLE IF NOT EXISTS alumnos
                  (id INTEGER PRIMARY KEY, nombre TEXT, edad INTEGER)''')

# Guardar los cambios y cerrar la conexión
conn.commit()
conn.close()


import sqlite3

def insert_alumnos(nombre, edad):
    conn = sqlite3.connect('Facultad.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO alumnos (nombre, edad) VALUES (?, ?)', (nombre, edad))
    conn.commit()
    conn.close()
