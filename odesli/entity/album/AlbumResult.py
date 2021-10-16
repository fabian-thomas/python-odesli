from __future__ import annotations

from ..EntityResult import EntityResult
from .Album import Album

"""
Represents the result when a album was requested.

albumLink:          Odesli album page url.
album:              Instance of Album. Provides title, artist, etc.
                    Represents the album corresponding to the provider
                    that was used for querying.
albumsByProvider:   Dictionary, mapping providers to the corresponding
                    albums (The attribute album is included in this dictionary).
"""
class AlbumResult(EntityResult):
    def __init__(self, albumLink, album, albumsByProvider):
        self.albumLink = albumLink
        self.album = album
        self.albumsByProvider = albumsByProvider

    @staticmethod
    def parse(result) -> AlbumResult:
        return AlbumResult(*super(AlbumResult, AlbumResult).parse(result, Album))

