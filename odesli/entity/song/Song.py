from __future__ import annotations

from ..Entity import Entity

"""
Represents a song for one provider.

id:                 Id of the song that's used by the provider.
provider:           The provider.
title:              The title of the song.
artistName:         The name of the artistName of this song.
thumbnailUrl:       The thumbnail url of the song.
thumbnailWidth:     The width of the thumbnail of the song.
thumbnailHeight:    The height of the thumbnail of the song.
linksByPlatform:    Dictionary, mapping platforms to links to this song.
                    Note that Platform != Provider. There is the provider youtube
                    with the two platforms youtube and youtubeMusic.

"""
class Song(Entity):
    def __init__(self, id, provider, title, artistName, thumbnailUrl, thumbnailWidth,
            thumbnailHeight, linksByPlatform):
        super().__init__(id, provider, title, artistName, thumbnailUrl, thumbnailWidth,
            thumbnailHeight, linksByPlatform)

    def getType(self):
        return 'song'

    @staticmethod
    def parse(rawSongEntity, linksByPlatform) -> Song:
        return Song(*Entity.parse(rawSongEntity, linksByPlatform))

    def __eq__(self, o):
        if isinstance(o, Song):
            return super().__eq__(o)
        return False
