import pytest
from main import suma, numMayor, login

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
        ("Ismael", "1234567", False),
        ("Ramon", "milanesa", False),
        ("Juancito", "belgrano", True)
    ]
)

def test_login_param(username, password, expected):
    assert login(username, password) == expected
    