from sql import DatabaseManager
from spotify import SpotifyWrapper


class SpotifyDBFiller:
    def __init__(self):
        self.dbmanager = DatabaseManager()
        self.wrapper = SpotifyWrapper()

    def get_tracks(self):
        return self.dbmanager.get_tracks()

    def get_track_spotify_id(self, track_name: str, album: str, artist: str):
        track_data = self.wrapper.search(f"{track_name} {album} {artist}")
        track_id = track_data['id']
        return track_id

    def get_audio_features(self, ids: list):
        return self.wrapper.get_audio_features(ids)

    def fill_tempos_in_db(self, db_ids: list, tempos: list):
        for d in zip(db_ids, tempos):
            id, tempo = d
            self.dbmanager.insert_data_from_spotify(id, tempo)



if __name__ == "__main__":
    spotify = SpotifyDBFiller()