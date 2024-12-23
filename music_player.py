"""
The question was to build a music player like Spotify with the following functionality: 
- add_song(song_title:string) - Adds song to catalog and generates an id starting with 1 
- play_song(song_id:int, user_id:int) - Tracks a song played and by a given user 
- print_summary() - Prints song names and how many unique listens it received sorted in descending order by unique listens 
- last_three_played_songs(user_id: int) Takes a userId and prints their last 3 played songs 
- Update print_summary method to only print k songs, and ensure all methods run better than O(N log N)
"""
from collections import defaultdict, deque

class MusicPlayer:
    def __init__(self):
        self.song_catalog = defaultdict()
        self.song_listen_count = defaultdict(set)
        self.song_counter = 0

    def add_song(self, song_title: str) -> int:
        self.song_counter += 1
        self.song_catalog[self.song_counter] = song_title
        return self.song_counter
    
    def play_song(self, song_id: int, user_id: int) -> None:
        if song_id not in self.song_catalog:
            raise ValueError("Invalid Song ID")
        self.song_listen_count[song_id].add(user_id)
    
    def print_summary(self, k: int = None) -> None:
        summary = [(song_id, len(users)) for song_id, users in self.song_listen_count.items()]
        summary.sort(key=lambda x: -x[1])

        for song_id, unique_count in summary:
            print(f"{self.song_catalog[song_id]}: {unique_count} unique listens")

if __name__ == "__main__":
    music_player = MusicPlayer()

    # Add songs
    song1 = music_player.add_song("Song A")
    song2 = music_player.add_song("Song B")
    song3 = music_player.add_song("Song C")
    song4 = music_player.add_song("Song D")

    # Users play songs
    music_player.play_song(song1, 1)  # User 1 plays Song A
    music_player.play_song(song2, 1)  # User 1 plays Song B
    music_player.play_song(song3, 1)  # User 1 plays Song C
    music_player.play_song(song1, 2)  # User 2 plays Song A
    music_player.play_song(song3, 2)  # User 2 plays Song C
    music_player.play_song(song1, 3)  # User 3 plays Song A
    music_player.play_song(song4, 3)  # User 3 plays Song D

        # Print summary
    print("\nTop Songs Summary:")
    music_player.print_summary(k=3)  # Print top 3 songs


"""
The first question is: "With our music system, what are the 3 API calls?"

1. `add_song()`: Add a song with its name
2. `listen_to_song()`: Listen to a song ( input the name of the song)
3. `analysis()`: Analyze the user who listened to the music (output: ranking of songs based on unique users listening quantity, sorted descending)
"""

class MusicSystem:
    def __init__(self):
        self.songs = {}  # Store songs: {song_name: set(users_who_listened)}
        
    def add_song(self, song_name):
        """Add a new song to the system"""
        if song_name not in self.songs:
            self.songs[song_name] = set()
            return f"Song '{song_name}' added successfully"
        return f"Song '{song_name}' already exists"
    
    def listen_to_song(self, song_name, user_id):
        """Record when a user listens to a song"""
        if song_name not in self.songs:
            return f"Song '{song_name}' not found"
        self.songs[song_name].add(user_id)
        return f"User {user_id} listened to '{song_name}'"
    
    def analysis(self):
        """Analyze and return songs ranked by unique listeners"""
        # Create list of (song_name, listener_count) tuples
        song_stats = [(song, len(listeners)) for song, listeners in self.songs.items()]
        # Sort by listener count in descending order
        song_stats.sort(key=lambda x: x[1], reverse=True)
        return song_stats

# Example usage:
if __name__ == "__main__":
    music_system = MusicSystem()
    
    # Adding songs
    music_system.add_song("Shape of You")
    music_system.add_song("Blinding Lights")
    music_system.add_song("Dance Monkey")
    
    # Users listening to songs
    music_system.listen_to_song("Shape of You", "user1")
    music_system.listen_to_song("Shape of You", "user2")
    music_system.listen_to_song("Blinding Lights", "user1")
    music_system.listen_to_song("Dance Monkey", "user3")
    
    # Get analysis
    rankings = music_system.analysis()
    print("\nSong Rankings by Unique Listeners:")
    for song, listeners in rankings:
        print(f"{song}: {listeners} listeners")






    