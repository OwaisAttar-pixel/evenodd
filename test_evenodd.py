from evenodd import evenodd

def test_even():
    assert evenodd.even_odd(4) == "Even number"

def test_odd():
    assert evenodd.even_odd(5) == "Odd number"