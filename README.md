# python-odesli

Odesli/Songlink API wrapper for python.

Currently using version `v1-alpha.1` of the Odesli API.

## Installation

```bash
pip install odesli
```

### From source

Install the PyPI package `build`:
```bash
pip install build
```

Then (from the root of the repo):
```bash
pip install dist/*.whl
```

## Usage

Convert Spotify link to Tidal and Youtube Music links:
```python
from odesli.Odesli import Odesli

odesli = Odesli()
result = odesli.getByUrl('https://open.spotify.com/track/1jJci4qxiYcOHhQR247rEU')

print(result.songsByProvider['tidal'].linksByPlatform['tidal'])
print(result.songsByProvider['youtube'].linksByPlatform['youtubeMusic'])
```

<img alt="class diagram" src="resources/classes.png"/>

For more information refer to the official [Odesli API documentation](https://www.notion.so/API-d0ebe08a5e304a55928405eb682f6741).

## Projects using this wrapper

- [odesli-cli](https://github.com/fabian-thomas/odesli-cli)
