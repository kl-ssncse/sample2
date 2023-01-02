from hello import add
from hello import sub


def test_add():
    assert 2 == add(-2, 4)
    
    
def test_sub():
    assert -6 == sub(-2, 4)
