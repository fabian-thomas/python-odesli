# Releasing

- bump version
- build PyPI packages
- upload PyPI packages
- update class diagram

## Dependencies

pip install build twine pylint

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
