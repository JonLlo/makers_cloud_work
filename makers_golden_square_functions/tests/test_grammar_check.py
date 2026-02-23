from lib.grammar_check import *


def test_grammar_check_correct():
    result = grammar_check("Hello there.")
    assert result == "All gramatically sound."
def test_grammar_check_incorrect_caps():
    result = grammar_check("hello there.")
    assert result == "Grammar needs improving."
def test_grammar_check_incorrect_punc():
    result = grammar_check("Hello there")
    assert result == "Grammar needs improving."
def test_grammar_check_incorrect_both():
    result = grammar_check("hello there")
    assert result == "Grammar needs improving."
