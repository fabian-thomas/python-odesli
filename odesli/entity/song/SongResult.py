from ..EntityResult import EntityResult
from .Song import Song

"""
Represents the result when a song was requested.

songLink:           Odesli song page url.
song:               Instance of Song. Provides title, artist, etc.
                    Represents the song corresponding to the provider
                    that was used for querying.
songsByProvider:    Dictionary, mapping providers to the corresponding
                    songs (The attribute song is included in this dictionary).
"""
class SongResult(EntityResult):
    def __init__(self, songLink, song, songsByProvider):
        self.songLink = songLink
        self.song = song
        self.songsByProvider = songsByProvider

    @staticmethod
    def parse(result):
        return SongResult(*super(SongResult, SongResult).parse(result, Song))

