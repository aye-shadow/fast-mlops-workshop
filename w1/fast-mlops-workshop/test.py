from calculator import add, subtract

def test_add():
    assert add(1, 2) == 3
    assert add(1, 0) == 1
    assert add(0, 0) == 0

def test_subtract():
    assert subtract(3, 2) == 1
    assert subtract(1, 0) == 1
    assert subtract(0, 0) == 0