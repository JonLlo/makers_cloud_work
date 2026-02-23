from lib.make_snippet import *

def test_snippet_with_six():
    snippet = make_snippet("Hi my name is Jonny and I am 27")
    assert snippet == "Hi my name is Jonny..."


def test_snippet_with_five():
    snippet = make_snippet("Hi my name is Jonny")
    assert snippet == "Hi my name is Jonny"

def test_snippet_with_none():
    snippet = make_snippet("")
    assert snippet == ""