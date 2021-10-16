# Releasing

- bump version
- build PyPI packages
- upload PyPI packages
- update class diagram

## Dependencies

```bash
pip install build twine pylint
```

## Building

```bash
python -m build
```

## Uploading to PyPI

```bash
twine upload dist/*{VERSION}*
```

## Generating class diagram

```bash
pyreverse -o png odesli
```

# Testing

```bash
python3 -m unittest discover -s tests
```

## Dependencies

```bash
pip install unittest
```
