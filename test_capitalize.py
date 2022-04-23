# test_capitalize.py

from app import capitalize_string

def test_capitalize_string2():
    """ test 11"""
    s = "helloworld"
    if not isinstance(s, str):
        raise TypeError('Please provide a string')
    return s.capitalize()

def test_capitalize_string():
    """ test 2"""
    assert capitalize_string('test') == 'Test'