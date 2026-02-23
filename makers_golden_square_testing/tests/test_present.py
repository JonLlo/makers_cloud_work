# File: tests/test_reminder.py

import pytest # <-- New code
from lib.present import *


#When we wrap an item we get it back when unwrapping

def test_unwrapping_wrapped_present():
    present = Present()
    present.wrap("ps5")
    result = present.unwrap()
    assert result == "ps5"

#When we don't wrap an item we get an error when trying to unwrap it

def test_unwrapping_unwrapped_present():
    present = Present()
    with pytest.raises(Exception) as e: # <-- New code
        present.unwrap()
    error_message = str(e.value) # <-- New code
    assert error_message == "No contents have been wrapped."

#When we wrap an item an item we get an error when trying to wrap it

def test_wrapping_wrapped_present():
    present = Present()
    present.wrap("ps5")
    with pytest.raises(Exception) as e: # <-- New code
        present.wrap("Rubix cube")
    error_message = str(e.value) # <-- New code
    assert error_message == "A contents has already been wrapped."






