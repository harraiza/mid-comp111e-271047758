class Song:
    def __init__(self,title,album,duration,artist):
        self.title=title
        self.album=album
        self.duration=duration
        self.artist=artist
    def get_title(self):
        return self.title
    def get_album(self):
        return self.album
    def get_duration(self):
        return self.duration
    def get_artist(self):
        return self.artist
    def set_title(self,title):
        self.title=title
    def set_album(self,album):
        self.album=album
    def set_duration(self,duration):
        self.duration=duration
    def set_artist(self,artist):
        self.artist=artist
class Playlist:
    def __init__(self,title,description):
        self.title=title
        self.description=description
        self.list=[]
    def add_song(self):
        self.list.append(Song(input("title:"),input("album:"),input("duration:"),input("artist:")))
    def remove_song(self,title):
        for song in self.list:
           if song.title == title:
               self.list.remove(song)
    def display(self):
        print(self.title)
        print(self.description)
        for song in self.list:
            print(song.get_title(),song.get_album(),song.get_duration(),song.get_artist())
class Library:
    def  __init__(self):
        self.list=[]
    def addplaylist(self):
        self.list.append(Playlist(input("title:"),input("description:")))
    def removeplaylist(self,title):
        for playlist in self.list:
            if playlist.title == title:
                self.list.remove(playlist)
    def display(self):
        for playlist in self.list:
            print(playlist.title)
            print(playlist.description)
            for song in playlist.list:
                print(song.get_title(),song.get_album(),song.get_duration(),song.get_artist())
    
