import unittest

from odesli.Odesli import Odesli
from odesli.entity.album.Album import Album

EXPECTED_TIDAL_ALBUM = Album('1317014', 'tidal', 'Oracular Spectacular', 'MGMT', 'https://resources.tidal.com/images/19e9ee55/da59/42b4/97c8/7ff47d5c8beb/640x640.jpg', 640, 640, { 'tidal': 'https://listen.tidal.com/album/1317014' })

class TestSong(unittest.TestCase):

    def check(self, result):
        self.assertEqual(result.albumLink, 'https://album.link/s/6mm1Skz3JE6AXneya9Nyiv')
        self.assertEqual(result.album.getType(), 'album')
        self.assertEqual(result.album.provider, 'spotify')
        self.assertEqual(result.albumsByProvider['tidal'], EXPECTED_TIDAL_ALBUM)

    def test_ByUrl(self):
        o = Odesli()
        song = o.getByUrl('https://open.spotify.com/album/6mm1Skz3JE6AXneya9Nyiv')
        self.check(song)

    def test_ById(self):
        o = Odesli()
        song = o.getById('6mm1Skz3JE6AXneya9Nyiv', 'spotify', 'album')
        self.check(song)

if __name__ == '__main__':
    unittest.main()
