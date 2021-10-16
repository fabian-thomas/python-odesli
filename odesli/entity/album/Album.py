from __future__ import annotations

from ..Entity import Entity

"""
Represents a album for one provider.

id:                 Id of the album that's used by the provider.
provider:           The provider.
title:              The title of the album.
artistName:         The name of the artistName of this album.
thumbnailUrl:       The thumbnail url of the album.
thumbnailWidth:     The width of the thumbnail of the album.
thumbnailHeight:    The height of the thumbnail of the album.
linksByPlatform:    Dictionary, mapping platforms to links to this album.
                    Note that Platform != Provider. There is the provider youtube
                    with the two platforms youtube and youtubeMusic.

"""
class Album(Entity):
    def __init__(self, id, provider, title, artistName, thumbnailUrl, thumbnailWidth,
            thumbnailHeight, linksByPlatform):
        super().__init__(id, provider, title, artistName, thumbnailUrl, thumbnailWidth,
            thumbnailHeight, linksByPlatform)

    def getType(self):
        return 'album'

    @staticmethod
    def parse(rawAlbumEntity, linksByPlatform) -> Album:
        return Album(*Entity.parse(rawAlbumEntity, linksByPlatform))

    def __eq__(self, o):
        if isinstance(o, Album):
            return super().__eq__(o)
        return False
