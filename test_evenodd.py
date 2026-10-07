from evenodd import even_odd

def test_even():
    assert even_odd(4) == "Even number"

def test_odd():
    assert even_odd(5) == "Odd number"