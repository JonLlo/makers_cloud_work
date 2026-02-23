from lib.gratitudes import *

'''
Test 1 - inital empty set of gratitdues
'''
def test_initially_gratitudes_empty():
    gratitudes = Gratitudes()
    result = gratitudes.format()

    assert result == "Be grateful for: "

'''
Test 2 - Adding 3 gratitudes
'''
def test_three_gratitudes():
    gratitudes = Gratitudes()
    gratitudes.add("friends")
    gratitudes.add("family")
    gratitudes.add("football")

    result = gratitudes.format()

    assert result == "Be grateful for: friends, family, football"

