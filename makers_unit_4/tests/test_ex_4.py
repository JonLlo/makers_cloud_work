from lib.ex_4 import *

def test_check_true():
    grammarStats = GrammarStats()
    result = grammarStats.check("Jonny")
    assert result == True
def test_check_false():
    grammarStats = GrammarStats()
    result = grammarStats.check("jonny")
    assert result == False
def check_pass_count():
    grammarStats = GrammarStats()
    grammarStats.check("jonny")
    grammarStats.check("Jonny")
    grammarStats.check("sally")
    grammarStats.check("Sally")
    grammarStats.check('nIAMH')
    result = grammarStats.percentage_good()
    assert result == 2
    





    
    
