from calculator import add, subtract

def test_add(a,b):
    assert add(2,3) == 5

def test_subtract(a,b):
    assert subtract(3,2) == 1

if __name__ == "__main__":
    test_add()
    test_subtract()
    print("All test passed!")