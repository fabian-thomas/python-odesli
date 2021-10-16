class Entity():
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

    def getType(self):
        raise NotImplementedError("Not implemented in base class.")


    @staticmethod
    def parse(entity, linksByPlatformParsed, initClass):
        # copy matching links for this songs platforms
        linksByPlatform = {}
        for platform in entity['platforms']:
            linksByPlatform[platform] = linksByPlatformParsed[platform]
        return initClass(entity.get('id', ''), entity.get('apiProvider', ''), entity.get('title', ''),
                entity.get('artistName', ''), entity.get('thumbnailUrl', ''),
                entity.get('thumbnailWidth', ''), entity.get('thumbnailHeight', ''), linksByPlatform)

    def __eq__(self, o):
        if isinstance(o, Entity):
            return (self.id == o.id and self and self.provider == o.provider and self.title == o.title
                   and self.artistName == o.artistName and self.thumbnailUrl == o.thumbnailUrl
                   and self.thumbnailWidth == o.thumbnailWidth and self.thumbnailHeight == o.thumbnailHeight
                   and self.linksByPlatform == o.linksByPlatform)
        return False

    def __str__(self):
        return \
"""id:              %s
provider:        %s
artistName:      %s
thumbnailUrl:    %s
thumbnailWidth:  %s
thumbnailHeight: %s
linksByPlatform: %s""" % (self.id, self.provider, self.artistName, self.thumbnailUrl, self.thumbnailWidth, self.thumbnailHeight, self.linksByPlatform)

