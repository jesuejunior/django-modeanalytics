# Django Mode Analytics








#### Package build


Bumping version, options are `major, minor and patch`.

```shell
    bumpversion patch setup.py modeanalytics/__init__.py
```

Preparing the package

```shell
    python setup.py sdist bdist_wheel
```

Checking if the package is good enough to PyPi
```shell
    twine check dist/*
```

Uploading the package to PyPi

```shell
    twine upload dist/*
```
