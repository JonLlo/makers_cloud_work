# {{PROBLEM}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem


As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.


## 2. Design the Class Interface

'''The interface of a class includes:

The name of the class. ✅
The design of its initializer, the parameters it takes, and their data types
The design of any properties the user will need to read or write, and their data types
The design of its public methods, including:
Their names and purposes
What parameters they take and the data types
What they return and that data type
Any other side effects they might have'''

```python


class SongTracker:

    def __init__(self):
     

    def add_song(self, song):
      

    def show_songs(self):
    




## 3. Create Examples as Tests

    def test_show_no_songs():
        songTracker = SongTracker()
        result = songTracker.show_songs()
        assert result == 'No songs'

    def test_add_and_show_songs():
        songTracker = SongTracker()
        songTracker.add_song("Hey Jude")
        songTracker.add_song("No More Heroes")       
        assert result == 
        "You have listened to the following tracks: \n 'Hey Jude' \n'No More Heroes'"


#4. Implement the Behaviour

...




## 3. Create Examples as Tests


_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
