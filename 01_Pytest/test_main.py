import pytest
import sqlite3
from main import suma, numMayor, login, usuarios
from DB_alumnos import insert_alumnos

def test_suma():
    assert suma(10,20) == 30
    
    
def test_numMayor():
    assert numMayor(100,20)


#TODO: Test con parametros
@pytest.mark.parametrize(
    "input_a, input_b, expected",
    [
        (5,1,6),
        (suma(2,4), suma(8,9),23),
        (30,20,50),
        (-5, 1, -4),
        (suma(2,5), suma(10,22), suma(7,32))
    ]
)

def test_suma_param(input_a, input_b, expected):
    assert suma(input_a, input_b) == expected



#TODO: Test Login

def test_login():
    assert login("rlozano","12345678") == True
    
# Test con parametros
@pytest.mark.parametrize (
    "username,password, expected",
    [
        ("pepito", "12345678", True),
        ("Ismael", "1234567ab", True),
        ("Ramoncito", "milanesa", True),
        ("Juancito", "belgrano", True)
    ]
)

def test_login_param(username, password, expected):
    assert login(username, password) == expected
    
    
#Test usuarios
#Compruebo la lista de usuarios
def test_usuarios():
    assert usuarios() == ["rlozano", "pepito", "juancito", "manolito"]
    
#Compruebo que no haya usuarios vacios
def test_usuarios_len():
    for usuario in usuarios():
        assert len(usuario) > 0

#Compruebo un usuarios especifico
def test_usuarios_especifico():
    assert "rlozano" in usuarios()
    
#TODO: Test DB Alumnos
def test_DB_alumnos():
     # Insertar un usuario
    insert_alumnos('Juan', 25)
    
    # Conectar a la base de datos y verificar que el usuario se haya insertado
    conn = sqlite3.connect('Facultad.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM alumnos WHERE nombre=? AND edad=?', ('Juan', 25))
    resultado = cursor.fetchall()
    conn.close()
    
    # Verificar que se haya encontrado el usuario
    assert resultado, "El usuario no se registro"
    
def test_DB_alumnos_especifico():
     # Conectar a la base de datos y verificar si el usuario se encuentra en la tabla
    conn = sqlite3.connect('Facultad.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM alumnos WHERE nombre=? AND edad=?', ('Juan', 25))  # Buscamos 'Pedro' en lugar de 'Juan'
    resultado = cursor.fetchall()
    conn.close()
    
    # Verificar si el usuario se encuentra en la tabla
    assert resultado, "El alumno no se encuentra en la base de datos"