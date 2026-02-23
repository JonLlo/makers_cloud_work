from lib.ex_2 import *
def test_get_most_common_letter():
    result = get_most_common_letter("the roof, the roof, the roof is on fire!")
    assert result == "o"


def test_get_most_common_letter_again():
    result = get_most_common_letter("the roof, the roof, the roof is on fire!")
    assert result == "o"