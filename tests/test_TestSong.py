import unittest

from odesli.Odesli import Odesli
from odesli.song.Song import Song

EXPECTED_YOUTUBE_SONG = Song('VHb_XIql_gU', 'youtube', 'Kids', 'MGMT - Topic', 'https://i.ytimg.com/vi/VHb_XIql_gU/hqdefault.jpg', 480, 360, { 'youtube': 'https://www.youtube.com/watch?v=VHb_XIql_gU', 'youtubeMusic': 'https://music.youtube.com/watch?v=VHb_XIql_gU' })

class TestSong(unittest.TestCase):

    def check(self, result):
        self.assertEqual(result.songLink, 'https://song.link/s/1jJci4qxiYcOHhQR247rEU')
        self.assertEqual(result.song.provider, 'spotify')
        self.assertEqual(result.songsByProvider['youtube'], EXPECTED_YOUTUBE_SONG)

    def test_ByUrl(self):
        o = Odesli()
        song = o.getByUrl('https://open.spotify.com/track/1jJci4qxiYcOHhQR247rEU?si=3ee4124fcf3444ab')
        self.check(song)

    def test_ById(self):
        o = Odesli()
        song = o.getById('1jJci4qxiYcOHhQR247rEU', 'spotify', 'song')
        self.check(song)

if __name__ == '__main__':
    unittest.main()
