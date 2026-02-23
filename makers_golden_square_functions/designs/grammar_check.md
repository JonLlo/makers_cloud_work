


#NOTE NOT DONE YET FOR THIS


# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can manage my time
I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
# EXAMPLE

def reading_time(text):

    """

    Parameters: (list all parameters and their types)
        text: a string containing text.

    Returns: (state the return value and its type)
        a string of the form "Estimated reading time: x minutes and y seconds", 
        where x and y are integers.

    Side effects: (state any side effects)
        This function doesn't print anything or have any other side-effects
    """
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

"""
Note: 200 words per 60 seconds
so x words per 60x/200 (0.3x) seconds
Given x words 
It returns a time of 0.3x seconds.

Given 20 words
It returns a time of 0.3*20 = 6 seconds
"""
reading_time("Python is a very high-level, general-purpose programming language. Its design philosophy emphasises code readability with the use of significant indentation.") => "Estimated reading time: 0 minutes and 6 seconds"

"""
Given a blank string value
It gives an error message

reading_time("") => throws an error
"""


```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.reading_time import *

'''


Given a string of 20 words

It returns a time of 0.3*20 = 6 seconds
'''

def test_reading_time_20_words():
    result = reading_time("Python is a very high-level, general-purpose programming language. Its design philosophy emphasises code readability with the use of significant indentation.")
    assert result == "Estimated reading time: 0 minutes and 6 seconds."


'''
Given a string of input value None

It returns an error
'''





def test_reading_time_no_input():
       
    with pytest.raises(Exception) as e: # <-- New code
        reading_time("")
    error_message = str(e.value) # <-- New code
    assert error_message == "No text to be read."


```

Ensure all test function names are unique, otherwise pytest will ignore them!
