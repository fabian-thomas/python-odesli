"""
Represents a song for one provider.

songId:             Id of the song that's used by the provider.
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
    def __init__(self, songId, provider, title, artistName, thumbnailUrl, thumbnailWidth,
            thumbnailHeight, linksByPlatform):
        self.songId = songId
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
        return Song(songEntity['id'], songEntity['apiProvider'], songEntity['title'],
                songEntity['artistName'], songEntity['thumbnailUrl'],
                songEntity['thumbnailWidth'], songEntity['thumbnailHeight'], linksByPlatform)
