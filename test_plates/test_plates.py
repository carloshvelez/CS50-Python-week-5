from plates import is_valid

def test_is_valid_len():
    assert is_valid("CSRT450") == False
    assert is_valid("C0") == False

def test_is_valid_first_two():
    assert is_valid("CSRE45") == True
    assert is_valid("C50S") == False
    assert is_valid("50SC") == False

def test_is_valid_medium_nums():
    assert is_valid("cs45re") == False
    assert is_valid("cst54") == True
    assert is_valid("cst054") == False

def test_is_valid_all():
    assert is_valid("CS50") == True
    assert is_valid("IMY450") == True

def test_is_valid_alphanumeric():
    assert is_valid("4550") == False
    assert is_valid("450imy") == False
    assert is_valid("im,54") == False
