from bank import value

def test_value_hello():
    assert value("Hello") == 0
    assert value("Hello, mr.") == 0

def test_value_h():
    assert value("hi") == 20
    assert value("hola") == 20

def test_value_anything():
    assert value("Carlos") == 100
    assert value("1985") == 100
    assert value("¿Cómo está?") == 100