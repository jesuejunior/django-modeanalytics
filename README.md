# Django Mode Analytics


This project was only tested on PostgreSQL


## How it works



### Installation

- Requirements
    - Django and pyscopg2

```shell
    pip install modeanalytics
```


### Configuration

You must set the follow vars in your django `settings`

```
    MODE_ORG: str = ""
    MODE_ACCESS_KEY: str = ""
    MODE_ACCESS_SECRET: str = ""
```
To generate these signature tokens, please look at [Mode Support](https://mode.com/help/articles/organizations/#white-label-embed-signature-tokens)


Add *modeanalytics* in your _INSTALLED_APPS_ tuple

``` 
    INSTALLED_APPS = [
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.messages",
        "django.contrib.staticfiles",
        "modeanalytics",
    ]
```



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
