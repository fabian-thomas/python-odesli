from .Entity import Entity

class EntityResult():
    @staticmethod
    def parse(result, initClass):
        # pre-process the returned links
        linksByPlatform = {}
        for platform in result['linksByPlatform']:
            linksByPlatform[platform] = result['linksByPlatform'][platform]['url']
        # parse songs and remember the entity that corresponds to the requested provider
        requestedEntity = None
        entityByProvider = {}
        for entityId in result['entitiesByUniqueId']:
            entity = Entity.parse(result['entitiesByUniqueId'][entityId], linksByPlatform, initClass)
            entityByProvider[entity.provider] = entity
            if entityId == result['entityUniqueId']:
                requestedEntity = entity
        return (result['pageUrl'], requestedEntity, entityByProvider)

