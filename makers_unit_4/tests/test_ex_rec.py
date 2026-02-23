from lib.ex_rec import *

def test_show_no_songs():
    songTracker = SongTracker()
    result = songTracker.show_songs()
    assert result == 'No songs'

def test_add_and_show_songs():
    songTracker = SongTracker()
    songTracker.add_song("Hey Jude")
    songTracker.add_song("No More Heroes")  
    result = songTracker.show_songs()   
    assert result == "You have listened to the following tracks: \n Hey Jude\n No More Heroes"