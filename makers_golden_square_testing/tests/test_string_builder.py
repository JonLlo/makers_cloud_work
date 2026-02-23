from lib.string_builder import *
'''
Test 1 - Initally reports a count of 0
'''

def test_initially_reports_empty():
    sb = StringBuilder()
    result = sb.output()
    assert result == ""

def test_size_initally_zero():
    sb = StringBuilder()
    result = sb.size()
    assert result == 0

def test_adding_some_strings():
    sb = StringBuilder()
    sb.add("Hello")
    sb.add(" I am coding ")
    sb.add("some stuff.")
    result = sb.output()
    assert result == "Hello I am coding some stuff."

def test_size_bigger_with_strings():
    sb = StringBuilder()
    sb.add("Hello")
    sb.add(" I am coding ")
    sb.add("some stuff.")
    result = sb.size()
    assert result == 29

