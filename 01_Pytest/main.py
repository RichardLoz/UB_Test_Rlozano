def suma (a,b):
    return a + b

def numMayor (a , b):
    return a > b


def login(username, password):
    if len(username) >= 6 and len(password) >= 8:
        return True
    else:
        return False
        