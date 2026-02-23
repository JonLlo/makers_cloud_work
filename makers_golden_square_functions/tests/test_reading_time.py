from lib.reading_time import *
import pytest

def test_reading_time_no_input():
       
    with pytest.raises(Exception) as e: # <-- New code
        reading_time("")
    error_message = str(e.value) # <-- New code
    assert error_message == "No text to be read."


def test_reading_time_20_words():
    result = reading_time("Python is a very high-level, general-purpose programming language. Its design philosophy emphasises code readability with the use of significant indentation.")
    assert result == "Estimated reading time: 0 minutes and 6 seconds."
