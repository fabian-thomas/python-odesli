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
class SongResult():
    def __init__(self, songLink, song, songsByProvider):
        self.songLink = songLink
        self.song = song
        self.songsByProvider = songsByProvider

    @staticmethod
    def parse(result):
        # pre-process the returned links
        linksByPlatform = {}
        for platform in result['linksByPlatform']:
            linksByPlatform[platform] = result['linksByPlatform'][platform]['url']
        # parse songs and remember the song that corresponds to the requested provider
        requestedSong = None
        songsByProvider = {}
        for songEntityId in result['entitiesByUniqueId']:
            song = Song.parse(result['entitiesByUniqueId'][songEntityId], linksByPlatform)
            songsByProvider[song.provider] = song
            if songEntityId == result['entityUniqueId']:
                requestedSong = song
        return SongResult(result['pageUrl'], requestedSong, songsByProvider)

