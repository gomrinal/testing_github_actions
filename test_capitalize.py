# test_capitalize.py

def capitalize_string(s):
    """ test 1"""
    if not isinstance(s, str):
        raise TypeError('Please provide a string')
    return s.capitalize()

def test_capitalize_string():
    """ test 2"""
    assert capitalize_string('test') == 'Test'