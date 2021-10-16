import requests
import json

from .entity.song.SongResult import SongResult
from .entity.album.AlbumResult import AlbumResult
from .entity.EntityResult import EntityResult

BASE_URL = 'https://api.song.link'
API_VERSION = 'v1-alpha.1'
ROOT = f'{BASE_URL}/{API_VERSION}'
LINKS_ENDPOINT = 'links'

class Odesli():
    def __init__(self, key=None):
        self.key = key

    def __get(self, params) -> EntityResult:
        if not self.key == None:
            params['key'] = self.key
        requestResult = requests.get(f'{ROOT}/{LINKS_ENDPOINT}', params=params)
        requestResult.raise_for_status()
        result = json.loads(requestResult.content.decode())
        resultType = next(iter(result['entitiesByUniqueId'].values()))['type']
        if resultType == 'song':
            return SongResult.parse(result)
        elif resultType == 'album':
            return AlbumResult.parse(result)
        else:
            raise NotImplementedError(f'Entities with type {resultType} are not supported yet.')


    def getByUrl(self, url) -> EntityResult:
        return self.__get({ 'url': url })

    def getById(self, id, platform, type) -> EntityResult:
        return self.__get({
            'id': id,
            'platform': platform,
            'type': type
        })
