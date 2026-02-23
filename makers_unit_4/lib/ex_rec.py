class SongTracker:

    def __init__(self):
        self.song_list = []
     

    def add_song(self, song):
        self.song_list.append(song)
      

    def show_songs(self):
        if self.song_list == []:
            return 'No songs'
        song_str = "You have listened to the following tracks: "
        for song in self.song_list:
            song_str +=  f'\n {song}'
     
        return song_str
    

