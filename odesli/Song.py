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
class Song():
    def __init__(self, id, provider, title, artistName, thumbnailUrl, thumbnailWidth,
            thumbnailHeight, linksByPlatform):
        self.id = id
        self.provider = provider
        self.title = title
        self.artistName = artistName
        self.thumbnailUrl = thumbnailUrl
        self.thumbnailWidth = thumbnailWidth
        self.thumbnailHeight = thumbnailHeight
        self.linksByPlatform = linksByPlatform

    @staticmethod
    def parse(songEntity, linksByPlatformParsed):
        # copy matching links for this songs platforms
        linksByPlatform = {}
        for platform in songEntity['platforms']:
            linksByPlatform[platform] = linksByPlatformParsed[platform]
        return Song(songEntity.get('id', ''), songEntity.get('apiProvider', ''), songEntity.get('title', ''),
                songEntity.get('artistName', ''), songEntity.get('thumbnailUrl', ''),
                songEntity.get('thumbnailWidth', ''), songEntity.get('thumbnailHeight', ''), linksByPlatform)
