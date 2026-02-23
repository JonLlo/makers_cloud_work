from lib.count_words import *

def test_count_words_five():
    count = count_words("I went to the shop")
    assert count == 5


def test_count_words_zero():
    count = count_words("")
    assert count == 0

