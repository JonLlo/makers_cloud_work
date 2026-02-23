from lib.report_length import *

def test_report_length_5():
    result = report_length("Jonny")
    assert result == "This string was 5 characters long."

def test_report_length_0():
    result = report_length("")
    assert result == "This string was 0 characters long."



