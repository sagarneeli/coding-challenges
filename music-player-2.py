from collections import defaultdict, deque

class MusicPlayer:
    """A music player system that tracks songs, user listening history, and play statistics."""
    def __init__(self):
        self.song_catalog = {}  # Maps song_id to song_title
        self.song_listens = defaultdict(set)  # Maps song_id to set of user_ids who listened
        self.user_play_history = defaultdict(deque)  # Maps user_id to deque of last 3 song_ids
        self.next_song_id = 1  # Incremental song_id generator

    def add_song(self, song_title):
        """Adds a song to the catalog and assigns it a unique ID."""
        song_id = self.next_song_id
        self.song_catalog[song_id] = song_title
        self.next_song_id += 1
        print(f"Song added: {song_title} with ID {song_id}")

    def play_song(self, song_id, user_id):
        """Tracks a song being played by a user."""
        if song_id not in self.song_catalog:
            print("Error: Song ID not found.")
            return

        # Add the user_id to the set of listeners for the song
        self.song_listens[song_id].add(user_id)

        # Update the user's play history (last 3 songs)
        history = self.user_play_history[user_id]
        if len(history) == 3:
            history.popleft()
        history.append(song_id)

        print(f"User {user_id} played song {self.song_catalog[song_id]}")

    def print_summary(self, k=None):
        """Prints song names and unique listens in descending order of unique listens."""
        # Create a list of (song_id, unique_listens) pairs
        summary = [(song_id, len(users)) for song_id, users in self.song_listens.items()]
        # Sort by unique listens (descending) and then by song_id (ascending)
        summary.sort(key=lambda x: (-x[1], x[0]))

        print("\nSong Summary:")
        for i, (song_id, unique_listens) in enumerate(summary):
            if k is not None and i >= k:
                break
            print(f"{self.song_catalog[song_id]}: {unique_listens} unique listens")

    def last_three_played_songs(self, user_id):
        """Prints the last three songs played by the user."""
        if user_id not in self.user_play_history or not self.user_play_history[user_id]:
            print(f"User {user_id} has no play history.")
            return

        print(f"Last 3 songs played by User {user_id}:")
        for song_id in list(self.user_play_history[user_id]):
            print(f"- {self.song_catalog[song_id]}")

# Example usage
if __name__ == "__main__":
    player = MusicPlayer()

    # Add songs
    player.add_song("Song A")
    player.add_song("Song B")
    player.add_song("Song C")

    # Play songs
    player.play_song(1, 101)
    player.play_song(2, 101)
    player.play_song(3, 102)
    player.play_song(1, 102)
    player.play_song(1, 101)

    # Print summary
    player.print_summary(k=2)

    # Last three played songs
    player.last_three_played_songs(101)
    player.last_three_played_songs(102)
