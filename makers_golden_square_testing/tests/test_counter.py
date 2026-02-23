from lib.counter import *
'''
Test 1 - Initally reports a count of 0
'''

def test_initially_reports_zero():
    counter = Counter()
    result = counter.report()
    assert result == "Counted to 0 so far."
def test_reports_three_additions():
    counter = Counter()
    counter.add(1)
    counter.add(2)
    counter.add(3)
    result = counter.report()
    assert result == "Counted to 6 so far."


